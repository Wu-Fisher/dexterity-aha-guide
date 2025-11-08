# SiliconFlow API 调试脚本使用指南

## 🎯 快速开始

### 1. 设置 API Key

```bash
# 方法1: 环境变量 (推荐)
export SILICONFLOW_API_KEY="sk-your-key-here"

# 方法2: 命令行参数
python scripts/test_api.py --api-key "sk-your-key-here"
```

### 2. 运行完整测试

```bash
python scripts/test_api.py
```

这会运行所有4个测试:
- ✅ API 连接测试
- ✅ 简单翻译功能测试
- ✅ Markdown 格式保护测试
- ✅ Token 计数和成本估算

### 3. 运行单个测试

```bash
# 只测试连接
python scripts/test_api.py --test connection

# 只测试翻译
python scripts/test_api.py --test translation

# 只测试格式保护
python scripts/test_api.py --test markdown

# 只测试 Token 计数
python scripts/test_api.py --test token
```

---

## 🔧 高级用法

### 使用不同模型

```bash
# 使用 DeepSeek-V3
python scripts/test_api.py \
    --model "deepseek-ai/DeepSeek-V3"

# 使用 Qwen2.5-72B
python scripts/test_api.py \
    --model "Qwen/Qwen2.5-72B-Instruct"
```

### 使用其他 API 服务

```bash
# 使用 DeepSeek 官方 API
python scripts/test_api.py \
    --api-base "https://api.deepseek.com" \
    --model "deepseek-chat" \
    --api-key "sk-deepseek-key"
```

---

## 📊 测试说明

### 测试 1: API 连接测试

验证:
- API 地址是否正确
- API Key 是否有效
- 网络连接是否正常
- 基本请求响应流程

### 测试 2: 简单翻译功能

测试内容:
- 中文到英文的基本翻译
- Markdown 格式的初步保留
- Token 使用统计

### 测试 3: Markdown 格式保护

重点验证:
- 代码块是否完整保留
- 链接格式是否正确
- 图片语法是否保持
- URL 是否未被翻译

### 测试 4: Token 计数

测试不同长度文本的:
- Token 消耗量
- 字符到 Token 的转换比例
- 成本估算参考

---

## 🐛 常见问题

### Q1: 连接超时

```
❌ 请求超时,请检查网络连接
```

**解决方法**:
1. 检查网络连接
2. 确认 API Base URL 是否正确
3. 尝试增加超时时间 (修改脚本中的 `timeout` 参数)

### Q2: 401 认证失败

```
❌ HTTP错误: 401
```

**解决方法**:
1. 检查 API Key 是否正确
2. 确认 API Key 未过期
3. 验证是否有足够的配额

### Q3: 模型不存在

```
❌ API响应格式异常
```

**解决方法**:
1. 检查模型名称是否正确
2. 参考 SiliconFlow 文档确认可用模型
3. 尝试使用默认模型: `Qwen/Qwen2.5-7B-Instruct`

---

## 📝 输出示例

```
🚀 ======================================================== 🚀
🚀                    API 完整测试套件                    🚀
🚀 ======================================================== 🚀

============================================================
📡 测试 1: API 连接测试
============================================================
API 地址: https://api.siliconflow.cn
模型名称: Qwen/Qwen2.5-7B-Instruct
API Key: sk-xxxxxxxx...xxxx

⏳ 发送测试请求...
✅ HTTP 状态码: 200
✅ API 连接成功!
响应内容: Yes, I can hear you! How can I assist you today?

============================================================
🌐 测试 2: 简单翻译功能
============================================================
原始文本:

# 欢迎使用灵巧手指南

这是一个测试文本...

⏳ 正在翻译...

✅ 翻译成功!

翻译结果:
# Welcome to the Dexterous Hand Guide

This is a test text...

📊 Token 使用:
   输入: 125
   输出: 98
   总计: 223

============================================================
📋 测试结果汇总
============================================================
✅ 通过  连接测试
✅ 通过  翻译功能
✅ 通过  格式保护
✅ 通过  Token计数

总计: 4/4 项测试通过

🎉 所有测试通过! API 配置正确,可以正常使用。
```

---

## 🔗 相关资源

- **SiliconFlow 文档**: https://docs.siliconflow.cn/
- **可用模型列表**: https://siliconflow.cn/models
- **价格说明**: https://siliconflow.cn/pricing
