#!/usr/bin/env python3
"""
SiliconFlow API 调试和验证脚本

用于测试 API 连接、验证配置、调试翻译功能
"""

import os
import sys
import json
import requests
import argparse
from typing import Dict, Any


class APITester:
    """API 测试工具"""

    def __init__(
        self,
        api_key: str,
        api_base: str = "https://api.siliconflow.cn",
        model: str = "Pro/deepseek-ai/DeepSeek-V3.1-Terminus"
    ):
        self.api_key = api_key
        self.api_base = api_base.rstrip('/')
        self.model = model

    def test_connection(self) -> bool:
        """测试1: API 连接测试"""
        print("\n" + "="*60)
        print("📡 测试 1: API 连接测试")
        print("="*60)

        print(f"API 地址: {self.api_base}")
        print(f"模型名称: {self.model}")
        print(f"API Key: {self.api_key[:10]}...{self.api_key[-4:]}")

        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        payload = {
            "model": self.model,
            "messages": [
                {"role": "user", "content": "Hello, can you hear me?"}
            ],
            "max_tokens": 50,
            "stream": False
        }

        try:
            print("\n⏳ 发送测试请求...")
            response = requests.post(
                f"{self.api_base}/v1/chat/completions",
                headers=headers,
                json=payload,
                timeout=30
            )

            print(f"✅ HTTP 状态码: {response.status_code}")

            if response.status_code == 200:
                result = response.json()
                print("✅ API 连接成功!")
                print(f"响应内容: {result['choices'][0]['message']['content'][:100]}...")
                return True
            else:
                print(f"❌ API 返回错误状态码: {response.status_code}")
                print(f"错误详情: {response.text}")
                return False

        except requests.exceptions.Timeout:
            print("❌ 请求超时,请检查网络连接")
            return False
        except requests.exceptions.RequestException as e:
            print(f"❌ 连接失败: {e}")
            return False
        except Exception as e:
            print(f"❌ 未知错误: {e}")
            return False

    def test_simple_translation(self) -> bool:
        """测试2: 简单翻译测试"""
        print("\n" + "="*60)
        print("🌐 测试 2: 简单翻译功能")
        print("="*60)

        test_text = """
# 欢迎使用灵巧手指南

这是一个测试文本,包含以下内容:

- 列表项1
- 列表项2

**加粗文本** 和 *斜体文本*
"""

        print(f"原始文本:\n{test_text}")

        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        messages = [
            {
                "role": "system",
                "content": "You are a professional translator. Translate Chinese to English while preserving Markdown formatting."
            },
            {
                "role": "user",
                "content": f"Translate to English:\n\n{test_text}"
            }
        ]

        payload = {
            "model": self.model,
            "messages": messages,
            "temperature": 0.3,
            "max_tokens": 500,
            "stream": False
        }

        try:
            print("\n⏳ 正在翻译...")
            response = requests.post(
                f"{self.api_base}/v1/chat/completions",
                headers=headers,
                json=payload,
                timeout=60
            )

            response.raise_for_status()
            result = response.json()

            translated = result['choices'][0]['message']['content']
            usage = result.get('usage', {})

            print("\n✅ 翻译成功!")
            print(f"\n翻译结果:\n{translated}")
            print(f"\n📊 Token 使用:")
            print(f"   输入: {usage.get('prompt_tokens', 'N/A')}")
            print(f"   输出: {usage.get('completion_tokens', 'N/A')}")
            print(f"   总计: {usage.get('total_tokens', 'N/A')}")

            return True

        except Exception as e:
            print(f"❌ 翻译失败: {e}")
            return False

    def test_markdown_preservation(self) -> bool:
        """测试3: Markdown 格式保护测试"""
        print("\n" + "="*60)
        print("📝 测试 3: Markdown 格式保护")
        print("="*60)

        test_text = """
将以下内容翻译为英文,但保持所有 Markdown 格式不变:

## 代码示例

```python
def hello():
    print("Hello World")
```

[链接文本](https://example.com)

![图片描述](./image.png)
"""

        print(f"测试文本:\n{test_text}")

        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        messages = [
            {
                "role": "system",
                "content": """You are a technical translator.
CRITICAL: Preserve ALL Markdown syntax exactly:
- Code blocks (```...```)
- Links ([text](url))
- Images (![alt](url))
Do NOT translate code, URLs, or file paths."""
            },
            {
                "role": "user",
                "content": test_text
            }
        ]

        payload = {
            "model": self.model,
            "messages": messages,
            "temperature": 0.1,
            "max_tokens": 800,
            "stream": False
        }

        try:
            print("\n⏳ 正在测试...")
            response = requests.post(
                f"{self.api_base}/v1/chat/completions",
                headers=headers,
                json=payload,
                timeout=60
            )

            response.raise_for_status()
            result = response.json()

            translated = result['choices'][0]['message']['content']

            print("\n✅ 测试完成!")
            print(f"\n结果:\n{translated}")

            # 验证关键格式
            checks = [
                ("代码块保留", "```python" in translated or "```" in translated),
                ("链接保留", "](https://example.com)" in translated),
                ("图片保留", "![" in translated and "](./image.png)" in translated),
            ]

            print("\n🔍 格式检查:")
            all_passed = True
            for name, passed in checks:
                status = "✅" if passed else "❌"
                print(f"   {status} {name}")
                if not passed:
                    all_passed = False

            return all_passed

        except Exception as e:
            print(f"❌ 测试失败: {e}")
            return False

    def test_token_counting(self) -> bool:
        """测试4: Token 计数测试"""
        print("\n" + "="*60)
        print("📊 测试 4: Token 计数和成本估算")
        print("="*60)

        test_sizes = [
            ("小文本 (50字)", "这是一个简短的测试文本。" * 10),
            ("中文本 (200字)", "这是一个中等长度的测试文本,用于验证 token 计数功能。" * 20),
        ]

        for size_name, text in test_sizes:
            print(f"\n📏 测试 {size_name}:")
            print(f"   字符数: {len(text)}")

            headers = {
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json"
            }

            payload = {
                "model": self.model,
                "messages": [
                    {"role": "user", "content": f"Translate to English: {text}"}
                ],
                "max_tokens": 1000,
                "stream": False
            }

            try:
                response = requests.post(
                    f"{self.api_base}/v1/chat/completions",
                    headers=headers,
                    json=payload,
                    timeout=60
                )

                response.raise_for_status()
                result = response.json()
                usage = result.get('usage', {})

                prompt_tokens = usage.get('prompt_tokens', 0)
                completion_tokens = usage.get('completion_tokens', 0)
                total_tokens = usage.get('total_tokens', 0)

                print(f"   输入 Token: {prompt_tokens}")
                print(f"   输出 Token: {completion_tokens}")
                print(f"   总计 Token: {total_tokens}")
                print(f"   字符/Token 比: {len(text)/prompt_tokens:.2f}")

            except Exception as e:
                print(f"   ❌ 测试失败: {e}")
                return False

        print("\n✅ Token 计数测试完成!")
        return True

    def run_all_tests(self) -> Dict[str, bool]:
        """运行所有测试"""
        print("\n" + "🚀 " + "="*56 + " 🚀")
        print("🚀" + " "*20 + "API 完整测试套件" + " "*20 + "🚀")
        print("🚀 " + "="*56 + " 🚀")

        results = {
            "连接测试": self.test_connection(),
            "翻译功能": self.test_simple_translation(),
            "格式保护": self.test_markdown_preservation(),
            "Token计数": self.test_token_counting(),
        }

        # 汇总结果
        print("\n" + "="*60)
        print("📋 测试结果汇总")
        print("="*60)

        for test_name, passed in results.items():
            status = "✅ 通过" if passed else "❌ 失败"
            print(f"{status}  {test_name}")

        total = len(results)
        passed = sum(results.values())
        print(f"\n总计: {passed}/{total} 项测试通过")

        if passed == total:
            print("\n🎉 所有测试通过! API 配置正确,可以正常使用。")
        else:
            print("\n⚠️  部分测试失败,请检查 API 配置和网络连接。")

        return results


def main():
    parser = argparse.ArgumentParser(
        description='SiliconFlow API 调试和验证工具'
    )
    parser.add_argument(
        '--api-key',
        type=str,
        default=None,
        help='API Key (也可通过 SILICONFLOW_API_KEY 环境变量设置)'
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
    parser.add_argument(
        '--test',
        type=str,
        choices=['all', 'connection', 'translation', 'markdown', 'token'],
        default='all',
        help='指定要运行的测试 (默认: all)'
    )

    args = parser.parse_args()

    # 获取 API Key
    api_key = args.api_key or os.getenv('SILICONFLOW_API_KEY') or os.getenv('DEEPSEEK_API_KEY')
    if not api_key:
        print("❌ 错误: 请提供 API Key")
        print("\n使用方法:")
        print("  1. 环境变量: export SILICONFLOW_API_KEY='your-key'")
        print("  2. 命令参数: --api-key 'your-key'")
        sys.exit(1)

    # 创建测试器
    tester = APITester(
        api_key=api_key,
        api_base=args.api_base,
        model=args.model
    )

    # 运行测试
    if args.test == 'all':
        tester.run_all_tests()
    elif args.test == 'connection':
        tester.test_connection()
    elif args.test == 'translation':
        tester.test_simple_translation()
    elif args.test == 'markdown':
        tester.test_markdown_preservation()
    elif args.test == 'token':
        tester.test_token_counting()


if __name__ == '__main__':
    main()
