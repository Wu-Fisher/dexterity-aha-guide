#!/usr/bin/env python3
"""
Markdown 自动翻译脚本
支持 SiliconFlow API、DeepSeek API 和 OpenAI 兼容接口
"""

import os
import re
import sys
import argparse
from pathlib import Path
from typing import List
import requests
import json
import time


class MarkdownTranslator:
    """Markdown 翻译器 - 保留格式,完整翻译"""

    def __init__(
        self,
        api_key: str,
        api_base: str = "https://api.siliconflow.cn",
        model: str = "Pro/deepseek-ai/DeepSeek-V3.1-Terminus",
        max_tokens: int = 8000
    ):
        """
        初始化翻译器

        Args:
            api_key: API 密钥 (SiliconFlow/DeepSeek/OpenAI)
            api_base: API 基础URL
                     - SiliconFlow: https://api.siliconflow.cn (默认)
                     - DeepSeek: https://api.deepseek.com
                     - OpenAI: https://api.openai.com
            model: 模型名称 (默认: Pro/deepseek-ai/DeepSeek-V3.1-Terminus)
            max_tokens: 单次翻译最大token数
        """
        self.api_key = api_key
        self.api_base = api_base.rstrip('/')
        self.model = model
        self.max_tokens = max_tokens

    def _call_api(self, messages: List[dict], temperature: float = 0.2, max_retries: int = 3) -> str:
        """
        调用 API (OpenAI 兼容接口),支持重试机制
        支持 SiliconFlow, DeepSeek, OpenAI 等

        Args:
            messages: 消息列表
            temperature: 温度参数 (降低以提高一致性)
            max_retries: 最大重试次数

        Returns:
            翻译后的文本
        """
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        payload = {
            "model": self.model,
            "messages": messages,
            "temperature": temperature,
            "max_tokens": self.max_tokens,
            "stream": False
        }

        last_error = None
        for attempt in range(max_retries):
            try:
                # 根据重试次数递增超时时间
                timeout = 180 + (attempt * 60)  # 180s -> 240s -> 300s

                if attempt > 0:
                    print(f"  🔄 第 {attempt + 1} 次重试 (超时设置: {timeout}s)...")
                    time.sleep(5 * attempt)  # 指数退避: 0s, 5s, 10s

                response = requests.post(
                    f"{self.api_base}/v1/chat/completions",
                    headers=headers,
                    json=payload,
                    timeout=timeout
                )
                response.raise_for_status()
                result = response.json()

                # 提取响应内容
                if 'choices' in result and len(result['choices']) > 0:
                    content = result['choices'][0]['message']['content']

                    # 打印token使用情况
                    if 'usage' in result:
                        usage = result['usage']
                        print(f"  📊 Token使用: 输入={usage.get('prompt_tokens', 0)}, "
                              f"输出={usage.get('completion_tokens', 0)}, "
                              f"总计={usage.get('total_tokens', 0)}")

                    return content
                else:
                    raise ValueError(f"API响应格式异常: {result}")

            except requests.exceptions.Timeout as e:
                last_error = e
                print(f"  ⏰ 请求超时 ({timeout}s)")
                if attempt < max_retries - 1:
                    continue
                else:
                    print(f"  ❌ 已达最大重试次数,放弃本次翻译")

            except requests.exceptions.HTTPError as e:
                last_error = e
                print(f"  ❌ HTTP错误: {e.response.status_code}")
                if hasattr(e, 'response') and e.response is not None:
                    try:
                        error_detail = e.response.json()
                        print(f"  错误详情: {json.dumps(error_detail, indent=2, ensure_ascii=False)}")
                    except:
                        print(f"  响应内容: {e.response.text}")

                # 5xx 错误可以重试,4xx 错误不重试
                if e.response.status_code >= 500 and attempt < max_retries - 1:
                    continue
                else:
                    raise

            except requests.exceptions.RequestException as e:
                last_error = e
                print(f"  ❌ 网络错误: {e}")
                if attempt < max_retries - 1:
                    continue
                else:
                    raise

        # 所有重试都失败
        if last_error:
            raise last_error

    def _translate_chunk(self, text: str, target_lang: str = "English") -> str:
        """
        翻译单个文本块,保持原始结构

        Args:
            text: 待翻译文本
            target_lang: 目标语言

        Returns:
            翻译后的文本
        """
        if not text.strip():
            return text

        # 改进的提示词 - 强调结构保持
        system_prompt = f"""You are a professional technical document translator specializing in Markdown.

CRITICAL REQUIREMENTS:
1. Translate ALL Chinese text to {target_lang}
2. Preserve EXACT Markdown structure:
   - Keep all headers (# ## ###)
   - Keep all lists (- * 1. 2.)
   - Keep all tables exactly as they are
   - Keep all code blocks unchanged (```...```)
   - Keep all links format: [translated text](original_url)
   - Keep all image syntax: ![translated_alt](original_url)
   - Keep all HTML tags and attributes unchanged
   - Keep all emoji and special symbols

3. DO NOT:
   - Add or remove any lines
   - Change the order of content
   - Translate URLs, file paths, or code
   - Add explanations or notes
   - Merge or split paragraphs

4. Output format:
   - Output ONLY the translated content
   - Maintain the SAME line structure as input
   - Keep all empty lines exactly as they are

Example:
Input:
```
## 标题
这是一段文字。
- 列表项
```

Output:
```
## Title
This is a paragraph.
- List item
```
"""

        user_prompt = f"{text}"

        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ]

        return self._call_api(messages)

    def translate_markdown(
        self,
        source_file: Path,
        target_file: Path,
        target_lang: str = "English",
        chunk_size: int = 10000  # 减小分块大小,避免超时
    ) -> None:
        """
        翻译整个 Markdown 文件

        Args:
            source_file: 源文件路径
            target_file: 目标文件路径
            target_lang: 目标语言
            chunk_size: 分块大小(字符数,默认10000)
        """
        print(f"📖 读取文件: {source_file}")
        content = source_file.read_text(encoding='utf-8')

        print(f"🔄 开始翻译 (目标语言: {target_lang})...")
        print(f"📏 文件大小: {len(content)} 字符")

        # 如果文件较小,直接翻译整个文件
        if len(content) < chunk_size:
            print(f"  ⏳ 翻译整个文档...")
            try:
                translated = self._translate_chunk(content, target_lang)
            except Exception as e:
                print(f"  ⚠️  翻译失败: {e}")
                print(f"  ℹ️  保留原文")
                translated = content
        else:
            # 按章节分割 (保持完整性)
            print(f"  📑 文档较大,按章节分割...")
            chunks = self._split_by_sections(content, chunk_size)
            print(f"  📊 分为 {len(chunks)} 个章节")

            translated_chunks = []
            for i, chunk in enumerate(chunks):
                print(f"\n  ⏳ 翻译第 {i+1}/{len(chunks)} 个章节... ({len(chunk)} 字符)")
                try:
                    translated_chunk = self._translate_chunk(chunk, target_lang)
                    translated_chunks.append(translated_chunk)

                    # 成功后短暂延迟,避免请求过快
                    if i < len(chunks) - 1:
                        time.sleep(2)
                except Exception as e:
                    print(f"  ⚠️  第 {i+1} 章节翻译失败: {e}")
                    print(f"  ℹ️  保留原文")
                    translated_chunks.append(chunk)

            translated = '\n\n'.join(translated_chunks)

        # 保存文件
        target_file.parent.mkdir(parents=True, exist_ok=True)
        target_file.write_text(translated, encoding='utf-8')

        print(f"✅ 翻译完成! 保存至: {target_file}")
        print(f"📏 译文大小: {len(translated)} 字符")

    def _split_by_sections(self, content: str, max_size: int) -> List[str]:
        """
        按章节分割内容,保持结构完整性
        优化策略: 优先按一级标题分割,超大章节按二级/三级标题细分

        Args:
            content: 待分割内容
            max_size: 最大块大小

        Returns:
            分割后的章节列表
        """
        chunks = []
        lines = content.split('\n')

        current_chunk = []
        current_size = 0

        for line in lines:
            # 检测标题级别
            h1_match = re.match(r'^#\s+', line)  # 一级标题
            h2_match = re.match(r'^#{2}\s+', line)  # 二级标题
            h3_match = re.match(r'^#{3}\s+', line)  # 三级标题

            should_split = False

            # 分割策略
            if h1_match and current_size > max_size * 0.3:
                # 遇到一级标题,且当前块达到30%大小,分割
                should_split = True
            elif h2_match and current_size > max_size * 0.5:
                # 遇到二级标题,且当前块达到50%大小,分割
                should_split = True
            elif h3_match and current_size > max_size * 0.8:
                # 遇到三级标题,且当前块达到80%大小,分割
                should_split = True
            elif current_size > max_size * 1.2:
                # 强制分割: 超过120%阈值,无论是否标题
                should_split = True
                print(f"  ⚠️  警告: 章节超大 ({current_size} 字符),强制分割")

            if should_split and current_chunk:
                chunks.append('\n'.join(current_chunk))
                current_chunk = []
                current_size = 0

            current_chunk.append(line)
            current_size += len(line) + 1  # +1 for newline

        # 保存最后一个块
        if current_chunk:
            chunks.append('\n'.join(current_chunk))

        # 打印分块信息
        print(f"  📊 分块详情:")
        for i, chunk in enumerate(chunks):
            chunk_lines = chunk.count('\n') + 1
            first_header = re.search(r'^#{1,3}\s+(.+)$', chunk, re.MULTILINE)
            header_text = first_header.group(1) if first_header else "无标题"
            print(f"     块 {i+1}: {len(chunk)} 字符, {chunk_lines} 行 - '{header_text[:30]}...'")

        return chunks


def main():
    parser = argparse.ArgumentParser(
        description='Markdown 自动翻译工具 (支持多种 AI 模型)'
    )
    parser.add_argument(
        'source',
        type=str,
        help='源 Markdown 文件路径'
    )
    parser.add_argument(
        'target',
        type=str,
        help='目标 Markdown 文件路径'
    )
    parser.add_argument(
        '--lang',
        type=str,
        default='English',
        help='目标语言 (默认: English)'
    )
    parser.add_argument(
        '--api-key',
        type=str,
        default=None,
        help='API Key (也可通过 SILICONFLOW_API_KEY 或 DEEPSEEK_API_KEY 环境变量设置)'
    )
    parser.add_argument(
        '--api-base',
        type=str,
        default='https://api.siliconflow.cn',
        help='API Base URL (默认: https://api.siliconflow.cn)'
    )
    parser.add_argument(
        '--model',
        type=str,
        default='Pro/deepseek-ai/DeepSeek-V3.1-Terminus',
        help='模型名称 (默认: Pro/deepseek-ai/DeepSeek-V3.1-Terminus)'
    )

    args = parser.parse_args()

    # 获取 API Key
    api_key = args.api_key or os.getenv('SILICONFLOW_API_KEY') or os.getenv('DEEPSEEK_API_KEY')
    if not api_key:
        print("❌ 错误: 请通过以下方式之一提供 API Key:")
        print("   1. 使用 --api-key 参数")
        print("   2. 设置 SILICONFLOW_API_KEY 环境变量")
        print("   3. 设置 DEEPSEEK_API_KEY 环境变量")
        sys.exit(1)

    print(f"🤖 使用模型: {args.model}")
    print(f"🌐 API 地址: {args.api_base}")

    # 初始化翻译器
    translator = MarkdownTranslator(
        api_key=api_key,
        api_base=args.api_base,
        model=args.model
    )

    # 执行翻译
    source_file = Path(args.source)
    target_file = Path(args.target)

    if not source_file.exists():
        print(f"❌ 错误: 源文件不存在: {source_file}")
        sys.exit(1)

    try:
        translator.translate_markdown(
            source_file=source_file,
            target_file=target_file,
            target_lang=args.lang
        )
    except Exception as e:
        print(f"❌ 翻译失败: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == '__main__':
    main()
