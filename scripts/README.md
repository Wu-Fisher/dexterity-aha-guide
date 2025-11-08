# Dexterity Manipulation Guide - Translation Scripts

## 📚 文件说明

- **translate_markdown.py**: 主翻译脚本,支持 SiliconFlow/DeepSeek/OpenAI API
- **test_api.py**: API 调试验证工具,用于测试配置是否正确
- **requirements.txt**: Python 依赖包列表

---

## 🚀 快速开始

### 1. 安装依赖

```bash
cd scripts
pip install -r requirements.txt
```

### 2. 测试 API 配置

```bash
# 设置 API Key
export SILICONFLOW_API_KEY="sk-your-key-here"

# 运行测试脚本
python test_api.py

# 预期输出:
# ✅ 通过  连接测试
# ✅ 通过  翻译功能
# ✅ 通过  格式保护
# ✅ 通过  Token计数
```

### 3. 翻译文档

```bash
# 翻译 README 为英文
python translate_markdown.py ../README.md ../docs/en/README.md --lang "English"
```

---

## 📖 详细文档

- **[TRANSLATION.md](../docs/TRANSLATION.md)**: 完整使用指南(中文)
- **[TEST_API.md](./TEST_API.md)**: API 测试脚本说明

---

## 🌐 支持的 API 服务

| 服务 | API Base | 推荐模型 | 价格 |
|------|----------|----------|------|
| **SiliconFlow** | `https://api.siliconflow.cn` | `Qwen/Qwen2.5-7B-Instruct` | ¥0.42/百万tokens |
| **DeepSeek** | `https://api.deepseek.com` | `deepseek-chat` | ¥1/百万tokens |
| **OpenAI** | `https://api.openai.com` | `gpt-4-turbo` | $10/百万tokens |

---

## 💡 常用命令

```bash
# 测试 API 连接
python test_api.py --test connection

# 翻译为英文 (SiliconFlow)
python translate_markdown.py ../README.md ../docs/en/README.md

# 翻译为日文 (DeepSeek)
python translate_markdown.py ../README.md ../docs/ja/README.md \
    --lang "Japanese" \
    --api-base "https://api.deepseek.com" \
    --model "deepseek-chat"

# 使用 OpenAI GPT-4
python translate_markdown.py ../README.md ../docs/en/README.md \
    --api-base "https://api.openai.com" \
    --model "gpt-4-turbo" \
    --api-key "sk-..."
```

---

## 🎯 特性

- ✅ 智能 Markdown 解析,保护代码/链接/图片
- ✅ 批量翻译,减少 API 调用次数
- ✅ 多 API 兼容 (SiliconFlow/DeepSeek/OpenAI)
- ✅ Token 使用统计
- ✅ 错误自动恢复
- ✅ 完整的测试套件

---

## 📞 获取帮助

- 查看 [详细文档](../docs/TRANSLATION.md)
- 提交 [Issue](https://github.com/Wu-Fisher/dexterity-aha-guide/issues)
- 邮件: wutfisher@outlook.com
