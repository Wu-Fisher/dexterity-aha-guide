# 🌐 自动翻译文档

本项目提供两种自动翻译方案,用于将中文 README 自动翻译为英文版本。

## 📋 方案对比

| 特性 | 方案一: 本地脚本 | 方案二: GitHub Actions |
|------|-----------------|----------------------|
| **执行方式** | 本地手动运行 | 自动触发 (推送时) |
| **适用场景** | 测试、手动更新 | 持续集成、自动化 |
| **API 配置** | 本地环境变量 | GitHub Secrets |
| **执行速度** | 立即执行 | 依赖 CI 队列 |
| **成本** | 自己控制 | 每次推送都可能触发 |

---

## 🚀 方案一: 本地 Python 脚本

### 📦 安装依赖

```bash
cd scripts
pip install -r requirements.txt
```

### 🔑 配置 API Key

#### 方法 1: 环境变量 (推荐)

```bash
# 使用 SiliconFlow (推荐)
export SILICONFLOW_API_KEY="sk-your-key-here"

# 或使用 DeepSeek
export DEEPSEEK_API_KEY="sk-your-key-here"

# Windows (PowerShell)
$env:SILICONFLOW_API_KEY="sk-your-key-here"

# Windows (CMD)
set SILICONFLOW_API_KEY=sk-your-key-here
```

#### 方法 2: 命令行参数

```bash
python translate_markdown.py README.md docs/en/README.md --api-key "sk-your-key-here"
```

### ▶️ 使用方法

#### 测试 API 连接 (首次使用必做!)

```bash
# 运行 API 测试脚本
python scripts/test_api.py

# 这会测试:
# ✅ API 连接是否正常
# ✅ 翻译功能是否工作
# ✅ Markdown 格式是否保留
# ✅ Token 使用量统计
```

#### 基础用法

```bash
# 翻译 README.md 为英文 (使用 SiliconFlow)
python scripts/translate_markdown.py \
    README.md \
    docs/en/README.md \
    --lang "English"

# 使用 DeepSeek API
python scripts/translate_markdown.py \
    README.md \
    docs/en/README.md \
    --lang "English" \
    --api-base "https://api.deepseek.com" \
    --model "deepseek-chat"
```

#### 高级用法

```bash
# 指定其他语言
python scripts/translate_markdown.py \
    README.md \
    docs/ja/README.md \
    --lang "Japanese"

# 使用其他 API (如 OpenAI)
python scripts/translate_markdown.py \
    README.md \
    docs/en/README.md \
    --api-base "https://api.openai.com" \
    --model "gpt-4" \
    --api-key "sk-..."
```

### 🎯 工作原理

1. **智能分段**: 自动识别 Markdown 结构,将文档分成多个块
2. **格式保护**: 保留所有 Markdown 语法、代码块、链接、图片等
3. **批量翻译**: 合并小块内容,减少 API 调用次数
4. **质量保证**: 使用专业的提示词确保翻译质量

### 📝 关键特性

```python
# 保护以下内容不被翻译:
✅ 代码块 (```)
✅ 行内代码 (`code`)
✅ 图片链接 (![alt](url))
✅ 超链接 ([text](url))
✅ HTML 标签 (<div>)
✅ URL 地址

# 翻译以下内容:
📝 标题
📝 段落文本
📝 列表项
📝 引用块
📝 表格内容
```

---

## 🤖 方案二: GitHub Actions 自动化

### 🔧 配置步骤

#### 1. 添加 GitHub Secret

1. 进入仓库的 **Settings** → **Secrets and variables** → **Actions**
2. 点击 **New repository secret**
3. 创建以下 Secret:

| Name | Value |
|------|-------|
| `SILICONFLOW_API_KEY` | 你的 SiliconFlow API Key (推荐) |
| `DEEPSEEK_API_KEY` | 你的 DeepSeek API Key (可选,作为备用) |

> 💡 **提示**: 只需配置其中一个即可,优先使用 `SILICONFLOW_API_KEY`

#### 2. Workflow 已就绪

我已经创建了 `.github/workflows/translate.yml`,它会在以下情况下自动运行:

- ✅ 每次推送到 `main` 分支且 `README.md` 发生变化
- ✅ 手动触发 (在 GitHub Actions 页面)

### 🎮 手动触发

1. 进入仓库的 **Actions** 标签页
2. 选择 **🌐 Auto Translate README** workflow
3. 点击 **Run workflow** 按钮
4. 可选:勾选 "强制重新翻译" 忽略缓存

### 📊 Workflow 流程说明

```yaml
触发条件:
  - README.md 变更并推送到 main
  - 手动触发

执行步骤:
  1️⃣ 检出代码
  2️⃣ 安装 Python 环境
  3️⃣ 安装依赖 (requests)
  4️⃣ 检测 README.md 是否变更
  5️⃣ 调用翻译脚本 (DeepSeek API)
  6️⃣ 修正英文版中的相对路径
  7️⃣ 检查翻译质量 (文件大小、行数)
  8️⃣ 提交翻译后的文件
  9️⃣ 推送回仓库
```

### 🔍 查看执行日志

推送代码后:

1. 进入 **Actions** 标签页
2. 找到最新的 workflow 运行记录
3. 点击查看详细日志和摘要

---

## 🔑 获取 API Key

本项目支持多个 API 服务,推荐使用 **SiliconFlow**(性价比高,免费额度多)

### 方案一: SiliconFlow (推荐)

#### 1. 注册账号
访问: https://siliconflow.cn/

#### 2. 创建 API Key
1. 登录后进入控制台
2. 找到 **API Keys** 页面
3. 点击 **创建 API Key**
4. 复制生成的 Key (格式: `sk-...`)

#### 3. 定价说明
- **Qwen/Qwen2.5-7B-Instruct**: ¥0.42 / 百万 tokens
- **deepseek-ai/DeepSeek-V3**: ¥1.33 / 百万 tokens
- 翻译一次完整 README ≈ ¥0.01-0.02 元

> 💡 **新用户福利**: 注册即送免费额度,足够翻译数百次!

### 方案二: DeepSeek

#### 1. 注册账号
访问: https://platform.deepseek.com/

#### 2. 创建 API Key
1. 登录后进入 **API Keys** 页面
2. 点击 **Create API Key**
3. 复制生成的 Key (格式: `sk-...`)

#### 3. 定价说明
- **deepseek-chat**: ¥1 / 百万 tokens (输入)
- 翻译一次完整 README ≈ 0.02-0.05 元

---

## 🛠️ 技术实现细节

### 核心算法逻辑

```python
class MarkdownTranslator:
    """
    核心翻译器类

    工作流程:
    1. 读取 Markdown 文件
    2. 智能分段 (保护代码、链接等)
    3. 批量调用 API 翻译
    4. 合并结果并保存
    """

    def _split_markdown(self, content: str):
        """
        分段策略:
        - 代码块: 整体保留
        - 标题/列表: 逐行处理
        - 纯文本: 合并翻译
        """

    def _call_api(self, messages: List[dict]):
        """
        API 调用:
        - 使用 OpenAI 兼容接口
        - 支持 DeepSeek / OpenAI / 其他模型
        - 自动重试机制
        """
```

### 提示词工程

```python
system_prompt = """You are a professional technical document translator.

CRITICAL RULES:
1. Preserve ALL Markdown syntax
2. Keep code blocks unchanged
3. Translate anchor text but keep URLs
4. Maintain technical accuracy
5. Output ONLY translated content
"""
```

### 错误处理

```python
try:
    translated = self._translate_text(chunk)
except APIError:
    # 失败时保留原文
    translated = original_text
```

---

## 📚 常见问题 FAQ

### Q1: 翻译质量如何?

**A**: DeepSeek 对中文技术文档的翻译质量很高,特别是:
- ✅ 保持 Markdown 格式完整
- ✅ 专业术语翻译准确
- ✅ 保留原文的技术风格

### Q2: API 调用会消耗多少?

**A**: 以本 README 为例 (~50KB):
- Token 数: 约 15,000 tokens
- 费用: ≈ ¥0.03 元
- 时间: 30-60 秒

### Q3: 如何使用其他 AI 模型?

**A**: 脚本支持任何 OpenAI 兼容接口:

```bash
# 使用 OpenAI GPT-4
python scripts/translate_markdown.py \
    README.md docs/en/README.md \
    --api-base "https://api.openai.com" \
    --model "gpt-4-turbo" \
    --api-key "sk-..."

# 使用本地 Ollama
python scripts/translate_markdown.py \
    README.md docs/en/README.md \
    --api-base "http://localhost:11434" \
    --model "llama3" \
    --api-key "dummy"  # Ollama 不需要 key
```

### Q4: GitHub Actions 失败怎么办?

**A**: 常见原因:

1. **Secret 未配置**: 检查 `DEEPSEEK_API_KEY` 是否设置
2. **API 额度不足**: 登录 DeepSeek 平台充值
3. **网络问题**: GitHub Actions 服务器可能暂时无法访问 API

查看详细错误:
```
Actions → 选择失败的运行 → 查看 "Translate to English" 步骤日志
```

### Q5: 能否翻译成多种语言?

**A**: 可以!只需修改 `--lang` 参数:

```bash
# 日语
python scripts/translate_markdown.py README.md docs/ja/README.md --lang "Japanese"

# 法语
python scripts/translate_markdown.py README.md docs/fr/README.md --lang "French"

# 德语
python scripts/translate_markdown.py README.md docs/de/README.md --lang "German"
```

---

## 🎯 最佳实践建议

### 本地开发流程

```bash
# 1. 编辑中文 README
vim README.md

# 2. 本地测试翻译
python scripts/translate_markdown.py README.md docs/en/README.md

# 3. 检查翻译结果
cat docs/en/README.md

# 4. 满意后推送
git add README.md docs/en/README.md
git commit -m "docs: update README and English translation"
git push
```

### CI/CD 自动化流程

```bash
# 1. 只编辑中文版
vim README.md

# 2. 推送中文版
git add README.md
git commit -m "docs: update Chinese README"
git push

# 3. GitHub Actions 自动翻译并推送英文版
# (无需手动操作)

# 4. Pull 最新代码 (包含自动生成的英文版)
git pull
```

### 成本控制建议

1. **开发阶段**: 使用本地脚本,手动触发
2. **稳定阶段**: 启用 GitHub Actions 自动化
3. **频繁更新**: 考虑设置 workflow 的触发条件,避免每次小改动都翻译

---

## 🔗 相关资源

- **DeepSeek API 文档**: https://api-docs.deepseek.com/
- **GitHub Actions 文档**: https://docs.github.com/en/actions
- **Markdown 语法**: https://www.markdownguide.org/

---

## 📞 获取帮助

遇到问题?

1. 📖 先查看本文档的 FAQ 部分
2. 🐛 提交 Issue: https://github.com/Wu-Fisher/dexterity-aha-guide/issues
3. 📧 邮件联系: wutfisher@outlook.com

---

<div align="center">

**🌐 让你的文档触达全球读者 | Powered by DeepSeek AI**

</div>
