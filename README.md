# 学术论文方法分析系统 / Academic Paper Methodology Analyzer

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

一个专为AI研究生设计的论文方法分析框架，帮助深入理解论文的方法部分，包括方法动机、设计逻辑、流程细节、优势与不足。

*A structured framework designed for AI research students to deeply analyze academic paper methodologies, including motivation, design logic, pipeline details, advantages, and limitations.*

---

## 📋 目录 / Table of Contents

- [功能特点](#功能特点--features)
- [快速开始](#快速开始--quick-start)
- [分析框架](#分析框架--analysis-framework)
- [使用方法](#使用方法--usage)
- [配置说明](#配置说明--configuration)
- [示例](#示例--examples)
- [贡献指南](#贡献指南--contributing)

---

## 🎯 功能特点 / Features

### 核心功能
- ✅ **结构化分析框架**：涵盖论文方法分析的6大核心维度
- ✅ **详细Pipeline解析**：重点关注方法流程的每一个技术细节
- ✅ **对比分析**：系统化对比不同方法的优劣
- ✅ **实验评估**：全面分析实验设计和结果
- ✅ **实践指导**：提供复现和应用的具体建议
- ✅ **速记总结**：生成便于记忆的核心要点

### 设计理念
- 🎓 **面向研究生**：适合AI领域研究生学习和研究使用
- 📊 **系统化**：标准化的6步分析流程
- 🔍 **深度优先**：特别强调方法设计的技术细节
- 💡 **实用性**：不仅理解论文，还提供实现指导
- 📝 **易用性**：提供模板和示例，快速上手

---

## 🚀 快速开始 / Quick Start

### 安装

```bash
# 克隆仓库
git clone https://github.com/XieLipei/AnalyticTaskScheduler.git
cd AnalyticTaskScheduler

# 可选：创建虚拟环境
python -m venv venv
source venv/bin/activate  # Linux/Mac
# 或者 venv\Scripts\activate  # Windows

# 安装依赖（如果有的话）
pip install -r requirements.txt  # 如果存在
```

### 基本使用

```python
from paper_analyzer import PaperAnalyzer

# 创建分析器实例
analyzer = PaperAnalyzer()

# 获取完整分析框架
framework = analyzer.get_full_framework()
print(framework)

# 生成论文分析模板
template = analyzer.generate_analysis_template("Your Paper Title")
print(template)

# 获取特定章节的分析提示
method_design = analyzer.get_analysis_prompt("2")  # 方法设计
print(method_design)

# 获取特定小节的分析提示
pipeline = analyzer.get_analysis_prompt("2", "a")  # 方法流程
print(pipeline)
```

### 运行示例

```bash
python paper_analyzer.py
```

---

## 📚 分析框架 / Analysis Framework

本系统提供6个核心分析维度，每个维度包含多个子项：

### 0. 摘要翻译 / Abstract Translation
将论文摘要翻译成中文，保持原意和专业术语的准确性。

### 1. 方法动机 / Method Motivation
- **a) 提出方法的原因**：阐述作者提出该方法的驱动力
- **b) 现有方法的痛点**：具体指出现有方法的局限性
- **c) 研究假设或直觉**：用简洁语言概括论文的核心假设

### 2. 方法设计 / Method Design ⭐ **最重要部分**
- **a) 方法流程总结**：详细的Pipeline（输入→处理→输出），包含每一步的具体操作和技术细节
- **b) 模型结构**：描述各模块的功能与协同工作方式
- **c) 公式/算法解释**：用通俗语言解释公式和算法的意义

### 3. 与其他方法对比 / Method Comparison
- **a) 本质不同**：与现有主流方法的本质区别
- **b) 创新点**：明确指出创新贡献
- **c) 适用场景**：分析方法的适用范围
- **d) 对比表格**：优点/缺点/改进点的系统对比

### 4. 实验表现与优势 / Experimental Performance
- **a) 验证方法**：实验设计和设置
- **b) 关键指标**：最具代表性的实验数据和结论
- **c) 优势场景**：优势最明显的场景和数据集
- **d) 局限性**：泛化能力、计算开销等方面的不足

### 5. 学习与应用 / Learning and Application
- **a) 开源与复现**：是否开源，复现的关键步骤
- **b) 实现细节**：超参数、数据预处理、训练技巧
- **c) 任务迁移**：迁移到其他任务的可能性和方法

### 6. 总结 / Summary
- **a) 核心思想**：一句话概括（不超过20字）
- **b) 速记版Pipeline**：3-5个关键步骤，使用自明性语言

---

## 💻 使用方法 / Usage

### 方法1：使用Python API

```python
from paper_analyzer import PaperAnalyzer

analyzer = PaperAnalyzer()

# 场景1：获取完整分析框架指导
print(analyzer.get_full_framework())

# 场景2：生成空白分析模板
template = analyzer.generate_analysis_template("Attention Is All You Need")
with open("my_analysis.md", "w", encoding="utf-8") as f:
    f.write(template)

# 场景3：查看特定章节的分析提示
# 例如，重点查看"方法设计"部分的要求
print(analyzer.get_analysis_prompt("2"))

# 场景4：查看特定小节的详细提示
# 例如，专门查看"方法流程"的分析要求
print(analyzer.get_analysis_prompt("2", "a"))
```

### 方法2：直接使用模板

1. 参考 `example_analysis.md` 查看完整的分析示例
2. 复制模板内容，替换为你要分析的论文
3. 按照每个章节的提示进行填写

### 方法3：自定义配置

编辑 `config.yaml` 文件来自定义分析行为：

```yaml
analysis_settings:
  language: "zh-CN"
  output_format: "markdown"
  detail_level: "comprehensive"

method_design_requirements:
  min_pipeline_steps: 3
  max_pipeline_steps: 10
  technical_detail_depth: "high"
```

---

## ⚙️ 配置说明 / Configuration

### 基本配置项

| 配置项 | 说明 | 可选值 |
|--------|------|--------|
| `language` | 分析语言 | `zh-CN`, `en` |
| `output_format` | 输出格式 | `markdown`, `json`, `text` |
| `detail_level` | 详细程度 | `comprehensive`, `standard`, `brief` |
| `technical_detail_depth` | 技术细节深度 | `high`, `medium`, `low` |

### 章节权重

可以在配置文件中调整各章节的重要性权重：

```yaml
section_weights:
  abstract_translation: 1
  method_motivation: 2
  method_design: 5      # 最重要
  method_comparison: 3
  experimental_performance: 3
  learning_and_application: 2
  summary: 2
```

---

## 📖 示例 / Examples

### 示例1：完整论文分析

查看 `example_analysis.md` 文件，这是对经典论文《Attention Is All You Need》的完整分析示例，展示了：
- 如何翻译和理解摘要
- 如何深入剖析Transformer的方法设计
- 如何进行系统化的方法对比
- 如何总结关键实验结果
- 如何提供实现和迁移建议

### 示例2：快速生成模板

```python
from paper_analyzer import PaperAnalyzer

analyzer = PaperAnalyzer()

# 为你的论文生成分析模板
my_paper = "BERT: Pre-training of Deep Bidirectional Transformers"
template = analyzer.generate_analysis_template(my_paper)

# 保存到文件
with open(f"{my_paper}_analysis.md", "w", encoding="utf-8") as f:
    f.write(template)

print(f"模板已生成：{my_paper}_analysis.md")
```

### 示例3：获取特定章节指导

```python
# 当你专注于分析方法设计时
method_design_guide = analyzer.get_analysis_prompt("2")
print(method_design_guide)

# 当你需要填写方法Pipeline时
pipeline_guide = analyzer.get_analysis_prompt("2", "a")
print(pipeline_guide)
```

---

## 🎓 使用建议 / Best Practices

### 1. 阅读论文的顺序
1. 先完整阅读论文全文，理解大意
2. 使用本框架的提示逐节分析
3. **重点关注第2节（方法设计）**，这是核心
4. 结合实验结果验证方法的有效性
5. 思考如何应用到自己的研究中

### 2. 填写模板的技巧
- **摘要翻译**：保持专业术语的准确性
- **方法Pipeline**：一定要详细，每步都要说清楚输入输出和技术细节
- **速记Pipeline**：使用通俗语言，不要直接用论文术语
- **对比表格**：要客观，优缺点都要列出
- **局限性**：不仅看论文承认的，也要找隐含的不足

### 3. 分析深度建议
- **初次阅读**：使用`detail_level: "standard"`
- **深入研究**：使用`detail_level: "comprehensive"`
- **快速浏览**：使用`detail_level: "brief"`

### 4. 方法设计部分的重点
这是最重要的部分（权重为5），需要特别详细：
- 至少3步，最多10步的Pipeline
- 每一步都要有：输入、操作、技术细节、输出
- 如果有公式，用通俗语言解释
- 如果有模块，说明各模块如何协同工作

---

## 📊 项目结构 / Project Structure

```
AnalyticTaskScheduler/
├── README.md                   # 本文件
├── paper_analyzer.py           # 核心分析模块
├── config.yaml                 # 配置文件
├── example_analysis.md         # 完整分析示例
├── LICENSE                     # 许可证
└── requirements.txt            # 依赖（如需要）
```

---

## 🤝 贡献指南 / Contributing

欢迎贡献！你可以：

1. **提交问题**：发现bug或有功能建议，请提交Issue
2. **改进示例**：分享你的论文分析案例
3. **完善框架**：提出更好的分析维度或提示
4. **翻译工作**：帮助翻译成其他语言

### 贡献流程
1. Fork 本仓库
2. 创建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 开启 Pull Request

---

## 📄 许可证 / License

本项目采用 MIT 许可证 - 详见 [LICENSE](LICENSE) 文件

---

## 📮 联系方式 / Contact

项目维护者：XieLipei

项目链接：[https://github.com/XieLipei/AnalyticTaskScheduler](https://github.com/XieLipei/AnalyticTaskScheduler)

---

## 🙏 致谢 / Acknowledgments

感谢所有为AI研究做出贡献的研究者和开发者！

---

## 📝 更新日志 / Changelog

### v1.0.0 (2026-02-03)
- ✨ 初始版本发布
- ✅ 完整的6维度分析框架
- ✅ Python API支持
- ✅ 模板生成功能
- ✅ 完整的示例分析（Transformer论文）
- ✅ 配置文件支持

---

**祝你的论文阅读和研究顺利！Happy Paper Reading! 📚🎓**
