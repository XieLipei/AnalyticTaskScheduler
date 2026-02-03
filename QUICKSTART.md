# 快速开始 / Quick Start Guide

## 30秒快速上手

```bash
# 1. 运行演示
python demo.py

# 2. 运行核心模块查看功能
python paper_analyzer.py

# 3. 生成你的第一个分析模板
python -c "from paper_analyzer import PaperAnalyzer; a = PaperAnalyzer(); open('my_paper_analysis.md', 'w', encoding='utf-8').write(a.generate_analysis_template('My Paper Title'))"
```

---

## 5分钟入门教程

### 步骤 1: 了解系统能做什么

运行演示脚本：
```bash
python demo.py
```

这会展示系统的所有核心功能。

### 步骤 2: 查看示例分析

打开并阅读 `example_analysis.md`，这是对 Transformer 论文的完整分析示例。

### 步骤 3: 生成你的分析模板

创建文件 `generate_template.py`：

```python
from paper_analyzer import PaperAnalyzer

# 替换为你要分析的论文标题
paper_title = "BERT: Pre-training of Deep Bidirectional Transformers"

analyzer = PaperAnalyzer()
template = analyzer.generate_analysis_template(paper_title)

# 保存到文件
filename = f"{paper_title.replace(':', '-')}_analysis.md"
with open(filename, "w", encoding="utf-8") as f:
    f.write(template)

print(f"✓ 模板已生成: {filename}")
print("请打开文件并开始填写！")
```

运行：
```bash
python generate_template.py
```

### 步骤 4: 开始填写分析

打开生成的模板文件，按照以下优先级填写：

1. **摘要翻译**（5-10分钟）
2. **方法设计 - 方法流程**（30-60分钟）⭐ 最重要！
3. **方法动机**（10-15分钟）
4. **方法对比**（15-20分钟）
5. **实验表现**（10-15分钟）
6. **学习应用**（10-15分钟）
7. **总结**（5-10分钟）

---

## 常见使用场景

### 场景 1: 我在读论文，想要结构化地理解方法

```python
from paper_analyzer import PaperAnalyzer

analyzer = PaperAnalyzer()

# 获取完整的分析框架作为阅读指南
framework = analyzer.get_full_framework()
print(framework)

# 保存到文件，边读论文边参考
with open("reading_guide.md", "w", encoding="utf-8") as f:
    f.write(framework)
```

### 场景 2: 我需要准备组会，要讲清楚论文的方法

```python
from paper_analyzer import PaperAnalyzer

analyzer = PaperAnalyzer()

# 重点查看"方法设计"部分的要求
print(analyzer.get_analysis_prompt("2"))

# 特别关注"方法流程"的详细要求
print(analyzer.get_analysis_prompt("2", "a"))
```

### 场景 3: 我要写论文，需要对比相关工作

```python
from paper_analyzer import PaperAnalyzer

analyzer = PaperAnalyzer()

# 查看"方法对比"章节的要求
print(analyzer.get_analysis_prompt("3"))

# 特别是对比表格的要求
print(analyzer.get_analysis_prompt("3", "d"))
```

### 场景 4: 我要复现论文，需要记录实现细节

```python
from paper_analyzer import PaperAnalyzer

analyzer = PaperAnalyzer()

# 查看"学习应用"章节
print(analyzer.get_analysis_prompt("5"))

# 生成模板记录复现过程
template = analyzer.generate_analysis_template("Paper to Reproduce")
with open("reproduction_notes.md", "w", encoding="utf-8") as f:
    f.write(template)
```

---

## 命令行工具

### 查看特定章节

```bash
# 查看方法设计章节
python -c "from paper_analyzer import PaperAnalyzer; print(PaperAnalyzer().get_analysis_prompt('2'))"

# 查看实验表现章节
python -c "from paper_analyzer import PaperAnalyzer; print(PaperAnalyzer().get_analysis_prompt('4'))"
```

### 生成模板

```bash
# 快速生成模板
python -c "
from paper_analyzer import PaperAnalyzer
import sys

if len(sys.argv) < 2:
    print('Usage: python -c \"...\" \"Paper Title\"')
    sys.exit(1)

title = ' '.join(sys.argv[1:])
analyzer = PaperAnalyzer()
template = analyzer.generate_analysis_template(title)
filename = f'{title.replace(\" \", \"_\")}_analysis.md'
with open(filename, 'w', encoding='utf-8') as f:
    f.write(template)
print(f'✓ Template generated: {filename}')
" "Your Paper Title"
```

---

## API 参考

### PaperAnalyzer 类

```python
from paper_analyzer import PaperAnalyzer

analyzer = PaperAnalyzer()
```

#### 主要方法

**1. get_full_framework()**
- 返回完整的分析框架
- 返回类型: `str`
- 用途: 了解整体结构，作为阅读指南

```python
framework = analyzer.get_full_framework()
```

**2. get_analysis_prompt(section, subsection=None)**
- 获取特定章节或小节的分析提示
- 参数:
  - `section`: 章节编号 ("0"-"6")
  - `subsection`: 小节字母 ("a", "b", "c", "d") (可选)
- 返回类型: `str`

```python
# 获取整个章节
section_2 = analyzer.get_analysis_prompt("2")

# 获取特定小节
subsection_2a = analyzer.get_analysis_prompt("2", "a")
```

**3. generate_analysis_template(paper_title)**
- 生成可填写的分析模板
- 参数:
  - `paper_title`: 论文标题
- 返回类型: `str`

```python
template = analyzer.generate_analysis_template("My Paper Title")
```

---

## 章节编号参考

| 编号 | 章节名称 | 说明 |
|------|----------|------|
| 0 | 摘要翻译 | Abstract Translation |
| 1 | 方法动机 | Method Motivation |
| 2 | 方法设计 | Method Design ⭐ 最重要 |
| 3 | 方法对比 | Method Comparison |
| 4 | 实验表现 | Experimental Performance |
| 5 | 学习应用 | Learning & Application |
| 6 | 总结 | Summary |

---

## 配置选项

编辑 `config.yaml` 来自定义行为：

```yaml
# 基本设置
analysis_settings:
  language: "zh-CN"  # 分析语言
  output_format: "markdown"  # 输出格式
  detail_level: "comprehensive"  # 详细程度

# 方法设计要求
method_design_requirements:
  min_pipeline_steps: 3  # 最少步骤数
  max_pipeline_steps: 10  # 最多步骤数
  technical_detail_depth: "high"  # 技术细节深度

# 章节权重
section_weights:
  method_design: 5  # 方法设计最重要
  # ... 其他配置
```

---

## 下一步

- 📖 阅读 [完整文档](README.md)
- 📘 查看 [详细使用指南](USAGE_GUIDE.md)
- 🎯 运行 `python demo.py` 查看所有功能
- 💡 查看 `example_analysis.md` 学习如何分析论文

---

## 获取帮助

遇到问题？

1. 查看 [USAGE_GUIDE.md](USAGE_GUIDE.md) 中的常见问题
2. 运行 `python demo.py` 了解功能
3. 查看 `example_analysis.md` 参考示例
4. 在 GitHub 提交 Issue

---

**开始你的论文分析之旅！📚**
