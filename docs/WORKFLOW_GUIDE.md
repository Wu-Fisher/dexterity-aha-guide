# GitHub Actions 自动翻译工作流使用指南

## 🎯 智能触发机制

新版工作流实现了**智能检测**,避免不必要的 API 调用:

### 自动触发场景

当你 `push` 到 `main` 分支并修改了 `README.md` 时:

| 场景 | 是否触发翻译 | 说明 |
|------|------------|------|
| ✅ **仅修改 README.md** | **是** | 正常翻译流程 |
| ❌ **同时修改 README.md + docs/en/README.md (手动更新)** | **否** | 检测到英文版手动更新,跳过 |
| ✅ **同时修改两者 (自动翻译提交)** | **是** | 识别为自动翻译提交,继续翻译 |

### 判断逻辑

工作流通过以下步骤智能判断:

```bash
1. 检查 README.md 是否变更
   ↓ 是
2. 检查 docs/en/README.md 是否也在同次提交中变更
   ↓ 是
3. 检查 commit message 是否包含 "Auto-translate"
   ↓ 否 (说明是手动更新)
4. ✋ 跳过自动翻译,避免覆盖你的手动修改
```

---

## 🚀 手动触发方式

### 方法一: GitHub Web 界面

1. 进入仓库页面
2. 点击 **Actions** 标签
3. 选择左侧 **🌐 Auto Translate README** 工作流
4. 点击右侧 **Run workflow** 按钮
5. 根据需要配置参数:

| 参数 | 说明 | 默认值 |
|------|------|--------|
| **force** | 强制重新翻译 (忽略所有检查) | `false` |
| **target_lang** | 目标语言 (支持任意语言) | `English` |
| **skip_if_recent** | 如果英文版最近更新则跳过 | `true` |

### 方法二: GitHub CLI

```bash
# 强制翻译为英文
gh workflow run translate.yml -f force=true

# 翻译为日语
gh workflow run translate.yml -f target_lang=Japanese

# 强制翻译为韩语 (忽略检查)
gh workflow run translate.yml -f force=true -f target_lang=Korean
```

---

## 📋 使用场景示例

### 场景 1: 日常更新中文 README

```bash
# 你只修改了 README.md
git add README.md
git commit -m "docs: 添加新的硬件介绍"
git push

# ✅ 工作流自动触发,翻译英文版
```

### 场景 2: 同时手动更新中英文

```bash
# 你同时修改了两个文件
git add README.md docs/en/README.md
git commit -m "docs: update both versions"
git push

# ✋ 工作流检测到英文版手动更新,跳过翻译
# 📊 在 Actions 中会看到: "跳过原因: 英文版已在本次提交中手动更新"
```

### 场景 3: 强制重新翻译所有内容

```bash
# 在 GitHub Actions 页面手动触发
# 勾选 force = true

# ✅ 无论如何都会执行翻译,覆盖现有英文版
```

### 场景 4: 翻译为其他语言

```bash
# 手动触发,设置 target_lang = Japanese
gh workflow run translate.yml -f target_lang=Japanese

# ✅ 翻译为日语并保存到 docs/en/README.md
# 💡 注意: 目前统一保存到 docs/en/ 目录
```

---

## 🔍 查看翻译结果

每次运行后,在 Actions 页面的 **Summary** 标签中会看到:

### ✅ 执行了翻译

```markdown
## 🌐 翻译任务报告

### ✅ 翻译已执行

- 📄 输出文件: `docs/en/README.md`
- 📊 文件大小: 45.2K
- 🌐 目标语言: English
- 🤖 使用模型: DeepSeek-V3.1-Terminus
- 🔧 API 服务: SiliconFlow
```

### ⏭️ 跳过了翻译

```markdown
## 🌐 翻译任务报告

### ⏭️ 已跳过翻译

**跳过原因**: 英文版已在本次提交中手动更新

💡 **提示**: 如需强制翻译,请使用 `workflow_dispatch` 并勾选 `force` 选项
```

---

## ⚙️ 高级配置

### 修改默认模型

编辑 `.github/workflows/translate.yml` 第 119 行:

```yaml
--model "Pro/deepseek-ai/DeepSeek-V3.1-Terminus"
# 改为其他模型,如:
--model "Qwen/Qwen2.5-7B-Instruct"
```

### 修改 API 服务商

修改第 118 行:

```yaml
--api-base "https://api.siliconflow.cn"
# 改为 DeepSeek:
--api-base "https://api.deepseek.com"
```

### 添加更多目标语言

可以扩展工作流支持多语言翻译:

```yaml
- name: 🌐 翻译为日语
  run: |
    python scripts/translate_markdown.py \
      README.md \
      docs/ja/README.md \
      --lang "Japanese"

- name: 🌐 翻译为韩语
  run: |
    python scripts/translate_markdown.py \
      README.md \
      docs/ko/README.md \
      --lang "Korean"
```

---

## 🛡️ 保护措施

工作流包含多重保护机制:

1. **手动更新保护**: 自动识别手动修改,避免覆盖
2. **提交检查**: 只在有实际变更时提交
3. **质量检查**: 对比文件大小和行数
4. **错误恢复**: API 调用失败时保留原文

---

## 💡 最佳实践

### ✅ 推荐做法

- **日常使用**: 只修改中文 README,让工作流自动翻译
- **紧急修正**: 如需修正英文表述,直接编辑 `docs/en/README.md` 并同时提交两个文件
- **大规模改版**: 使用 `force=true` 强制重新翻译

### ❌ 避免的做法

- ~~单独修改英文版后再修改中文版~~ (会导致两次翻译,浪费 API 调用)
- ~~频繁手动触发~~ (有智能检测,无需频繁手动干预)

---

## 📞 故障排查

### 问题: 翻译没有触发

**检查清单**:
1. 查看 Actions 页面的日志
2. 确认 README.md 真的有变更 (`git diff HEAD^ HEAD README.md`)
3. 检查是否同时修改了英文版 (工作流会跳过)
4. 尝试手动触发 `force=true`

### 问题: API 调用失败

**可能原因**:
1. `SILICONFLOW_API_KEY` 或 `DEEPSEEK_API_KEY` secret 未设置
2. API 配额用尽
3. 网络问题

**解决方法**:
- 前往 **Settings → Secrets and variables → Actions** 检查 secrets
- 查看 API 服务商的配额剩余
- 使用本地脚本测试: `python scripts/test_api.py`

---

## 📚 相关文档

- [翻译脚本使用指南](TRANSLATION.md)
- [API 测试工具说明](../scripts/TEST_API.md)
- [脚本快速开始](../scripts/README.md)

---

**Made with ❤️ by the Dexterity Community**
