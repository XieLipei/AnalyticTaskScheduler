"""
Academic Paper Methodology Analyzer

This module provides a structured framework for analyzing academic papers,
specifically focusing on methodology sections. Designed for AI research students
to deeply understand paper methods, design logic, advantages, and limitations.
"""

class PaperAnalyzer:
    """
    Analyzes academic papers with a structured approach covering:
    0. Abstract Translation
    1. Method Motivation
    2. Method Design
    3. Method Comparison
    4. Experimental Performance
    5. Learning and Application
    6. Summary
    """
    
    def __init__(self):
        self.analysis_framework = self._initialize_framework()
    
    def _initialize_framework(self):
        """Initialize the comprehensive analysis framework."""
        return {
            "0_abstract_translation": {
                "description": "翻译摘要原文",
                "prompt": "请将论文摘要完整翻译成中文，保持原意和专业术语准确性。"
            },
            "1_method_motivation": {
                "description": "方法动机",
                "sections": {
                    "a": {
                        "title": "提出方法的原因",
                        "prompt": "作者为什么提出这个方法？阐述其背后的驱动力。"
                    },
                    "b": {
                        "title": "现有方法的痛点",
                        "prompt": "现有方法的痛点/不足是什么？具体指出局限性。"
                    },
                    "c": {
                        "title": "研究假设或直觉",
                        "prompt": "论文的研究假设或直觉是什么？用简洁语言概括。"
                    }
                }
            },
            "2_method_design": {
                "description": "方法设计",
                "sections": {
                    "a": {
                        "title": "方法流程总结",
                        "prompt": "给出清晰的方法流程总结（pipeline），逐步解释输入→处理→输出。必须讲清楚每一步的具体操作和技术细节。这一步必须非常细致，这是用户的主要阅读目标。"
                    },
                    "b": {
                        "title": "模型结构",
                        "prompt": "如果涉及模型结构，请描述每个模块的功能与作用，以及它们如何协同工作。"
                    },
                    "c": {
                        "title": "公式/算法解释",
                        "prompt": "如果有公式/算法，请用通俗语言解释它们的意义和在方法中的角色。"
                    }
                }
            },
            "3_method_comparison": {
                "description": "与其他方法对比",
                "sections": {
                    "a": {
                        "title": "本质不同",
                        "prompt": "本方法和现有主流方法相比，有什么本质不同？"
                    },
                    "b": {
                        "title": "创新点",
                        "prompt": "创新点在哪里？明确指出贡献度。"
                    },
                    "c": {
                        "title": "适用场景",
                        "prompt": "在什么场景下更适用？分析其适用范围。"
                    },
                    "d": {
                        "title": "方法对比表格",
                        "prompt": "用表格总结方法对比（优点/缺点/改进点），确保对比项清晰。"
                    }
                }
            },
            "4_experimental_performance": {
                "description": "实验表现与优势",
                "sections": {
                    "a": {
                        "title": "验证方法有效性",
                        "prompt": "作者如何验证该方法的有效性？描述实验设计和设置。"
                    },
                    "b": {
                        "title": "关键指标与数据",
                        "prompt": "实验结果在哪些指标上超越了对比方法？列出几个最具代表性的关键数据和结论。"
                    },
                    "c": {
                        "title": "优势明显的场景",
                        "prompt": "哪些场景/数据集下优势最明显？提供具体证据。"
                    },
                    "d": {
                        "title": "局限性",
                        "prompt": "是否有局限性（比如泛化能力、计算开销、对特定数据的依赖）？指出论文中承认或隐含的不足。"
                    }
                }
            },
            "5_learning_and_application": {
                "description": "学习与应用",
                "sections": {
                    "a": {
                        "title": "开源与复现",
                        "prompt": "论文是否开源？如果我想实现/复现这个方法，关键步骤是什么？"
                    },
                    "b": {
                        "title": "实现细节",
                        "prompt": "需要注意哪些超参数、数据预处理、训练细节？提供实现层面的建议。"
                    },
                    "c": {
                        "title": "迁移到其他任务",
                        "prompt": "该方法能否迁移到其他任务？如果能，如何迁移？"
                    }
                }
            },
            "6_summary": {
                "description": "总结",
                "sections": {
                    "a": {
                        "title": "核心思想",
                        "prompt": "用一句话概括这个方法的核心思想（不超过20字）。"
                    },
                    "b": {
                        "title": "速记版pipeline",
                        "prompt": "给出一个'速记版pipeline'（使用3-5个关键步骤），方便记忆。这个pipeline不要使用论文使用的专业词汇，而是应当具有自明性，让读者只看pipeline即可大体理解论文内容。不要用比喻，直白的讲出内容。"
                    }
                }
            }
        }
    
    def get_analysis_prompt(self, section=None, subsection=None):
        """
        Get the analysis prompt for a specific section or subsection.
        
        Args:
            section: Main section number (e.g., "1", "2", "3")
            subsection: Subsection letter (e.g., "a", "b", "c")
        
        Returns:
            str: The prompt text for the specified section
        """
        if section is None:
            return self.get_full_framework()
        
        section_key = f"{section}_" + self._get_section_name(section)
        
        if section_key not in self.analysis_framework:
            return f"Section {section} not found"
        
        section_data = self.analysis_framework[section_key]
        
        if subsection is None:
            if "sections" in section_data:
                result = f"## {section}. {section_data['description']}\n\n"
                for sub_key, sub_data in section_data["sections"].items():
                    result += f"### {section}{sub_key}) {sub_data['title']}\n"
                    result += f"{sub_data['prompt']}\n\n"
                return result
            else:
                return f"## {section}. {section_data['description']}\n{section_data.get('prompt', '')}\n"
        else:
            if "sections" in section_data and subsection in section_data["sections"]:
                sub_data = section_data["sections"][subsection]
                return f"## {section}{subsection}) {sub_data['title']}\n{sub_data['prompt']}\n"
            else:
                return f"Subsection {section}{subsection} not found"
    
    def _get_section_name(self, section):
        """Get the section name key from section number."""
        section_map = {
            "0": "abstract_translation",
            "1": "method_motivation",
            "2": "method_design",
            "3": "method_comparison",
            "4": "experimental_performance",
            "5": "learning_and_application",
            "6": "summary"
        }
        return section_map.get(section, "")
    
    def get_full_framework(self):
        """
        Get the complete analysis framework as a formatted string.
        
        Returns:
            str: Complete analysis framework with all sections and prompts
        """
        result = "# 学术论文方法分析框架\n\n"
        result += "## 角色定位\n"
        result += "你是一名AI领域的研究生，目标是深入理解论文的方法部分，"
        result += "包括方法动机、设计逻辑、流程细节、优势与不足，以便学习和在研究中借鉴。"
        result += "你的角色是高效、深入的论文分析师。\n\n"
        
        for key, value in self.analysis_framework.items():
            section_num = key.split("_")[0]
            result += f"## {section_num}. {value['description']}\n\n"
            
            if "prompt" in value:
                result += f"{value['prompt']}\n\n"
            
            if "sections" in value:
                for sub_key, sub_value in value["sections"].items():
                    result += f"### {section_num}{sub_key}) {sub_value['title']}\n"
                    result += f"{sub_value['prompt']}\n\n"
        
        return result
    
    def generate_analysis_template(self, paper_title="论文标题"):
        """
        Generate a template for paper analysis that can be filled in.
        
        Args:
            paper_title: Title of the paper to analyze
        
        Returns:
            str: Analysis template with placeholders
        """
        template = f"# 论文分析：{paper_title}\n\n"
        template += "---\n\n"
        
        template += "## 0. 摘要翻译\n\n"
        template += "[在此填写中文翻译的摘要]\n\n"
        template += "---\n\n"
        
        template += "## 1. 方法动机\n\n"
        template += "### a) 提出方法的原因\n\n"
        template += "[作者为什么提出这个方法？阐述其背后的驱动力]\n\n"
        template += "### b) 现有方法的痛点\n\n"
        template += "[现有方法的痛点/不足是什么？具体指出局限性]\n\n"
        template += "### c) 研究假设或直觉\n\n"
        template += "[论文的研究假设或直觉是什么？用简洁语言概括]\n\n"
        template += "---\n\n"
        
        template += "## 2. 方法设计\n\n"
        template += "### a) 方法流程总结（Pipeline）\n\n"
        template += "**这是最重要的部分，需要非常详细地说明每一步**\n\n"
        template += "1. **输入**：\n"
        template += "   - [描述输入数据的类型、格式、特征]\n\n"
        template += "2. **处理步骤1**：\n"
        template += "   - [详细描述第一步的具体操作和技术细节]\n\n"
        template += "3. **处理步骤2**：\n"
        template += "   - [详细描述第二步的具体操作和技术细节]\n\n"
        template += "4. **处理步骤N**：\n"
        template += "   - [继续添加处理步骤...]\n\n"
        template += "5. **输出**：\n"
        template += "   - [描述输出结果的类型、格式]\n\n"
        template += "### b) 模型结构\n\n"
        template += "[如果涉及模型结构，描述每个模块的功能与作用，以及它们如何协同工作]\n\n"
        template += "### c) 公式/算法解释\n\n"
        template += "[如果有公式/算法，用通俗语言解释它们的意义和在方法中的角色]\n\n"
        template += "---\n\n"
        
        template += "## 3. 与其他方法对比\n\n"
        template += "### a) 本质不同\n\n"
        template += "[本方法和现有主流方法相比，有什么本质不同？]\n\n"
        template += "### b) 创新点\n\n"
        template += "[创新点在哪里？明确指出贡献度]\n\n"
        template += "### c) 适用场景\n\n"
        template += "[在什么场景下更适用？分析其适用范围]\n\n"
        template += "### d) 方法对比表格\n\n"
        template += "| 方法 | 优点 | 缺点 | 改进点 |\n"
        template += "|------|------|------|--------|\n"
        template += "| 现有方法A | [填写] | [填写] | - |\n"
        template += "| 现有方法B | [填写] | [填写] | - |\n"
        template += "| **本文方法** | [填写] | [填写] | [填写] |\n\n"
        template += "---\n\n"
        
        template += "## 4. 实验表现与优势\n\n"
        template += "### a) 验证方法有效性\n\n"
        template += "[作者如何验证该方法的有效性？描述实验设计和设置]\n\n"
        template += "### b) 关键指标与数据\n\n"
        template += "[实验结果在哪些指标上超越了对比方法？列出几个最具代表性的关键数据和结论]\n\n"
        template += "**关键结果示例**：\n"
        template += "- 指标1: 提升X%\n"
        template += "- 指标2: 达到Y\n"
        template += "- 指标3: 优于基线Z\n\n"
        template += "### c) 优势明显的场景\n\n"
        template += "[哪些场景/数据集下优势最明显？提供具体证据]\n\n"
        template += "### d) 局限性\n\n"
        template += "[是否有局限性（比如泛化能力、计算开销、对特定数据的依赖）？指出论文中承认或隐含的不足]\n\n"
        template += "---\n\n"
        
        template += "## 5. 学习与应用\n\n"
        template += "### a) 开源与复现\n\n"
        template += "- **是否开源**：[是/否]\n"
        template += "- **代码链接**：[如有]\n"
        template += "- **复现关键步骤**：\n"
        template += "  1. [步骤1]\n"
        template += "  2. [步骤2]\n"
        template += "  3. [步骤N]\n\n"
        template += "### b) 实现细节\n\n"
        template += "**需要注意的要点**：\n"
        template += "- **超参数**：[列出关键超参数及推荐值]\n"
        template += "- **数据预处理**：[描述预处理步骤]\n"
        template += "- **训练细节**：[优化器、学习率、batch size等]\n\n"
        template += "### c) 迁移到其他任务\n\n"
        template += "[该方法能否迁移到其他任务？如果能，如何迁移？]\n\n"
        template += "---\n\n"
        
        template += "## 6. 总结\n\n"
        template += "### a) 核心思想（不超过20字）\n\n"
        template += "[一句话概括这个方法的核心思想]\n\n"
        template += "### b) 速记版Pipeline（3-5个关键步骤）\n\n"
        template += "**注意：使用自明性语言，不用专业术语，让读者只看pipeline即可大体理解论文内容**\n\n"
        template += "1. [步骤1：直白描述]\n"
        template += "2. [步骤2：直白描述]\n"
        template += "3. [步骤3：直白描述]\n"
        template += "4. [步骤4：直白描述（如需要）]\n"
        template += "5. [步骤5：直白描述（如需要）]\n\n"
        template += "---\n\n"
        template += "**分析完成日期**：[填写日期]\n"
        
        return template


def main():
    """Demonstration of the PaperAnalyzer usage."""
    analyzer = PaperAnalyzer()
    
    print("=" * 80)
    print("学术论文方法分析系统")
    print("Academic Paper Methodology Analyzer")
    print("=" * 80)
    print("\n使用方法示例：\n")
    
    # Example 1: Get full framework
    print("1. 获取完整分析框架：")
    print("-" * 80)
    framework = analyzer.get_full_framework()
    print(framework[:500] + "...\n")
    
    # Example 2: Get specific section
    print("\n2. 获取特定章节（例如：方法设计）：")
    print("-" * 80)
    section_2 = analyzer.get_analysis_prompt("2")
    print(section_2[:300] + "...\n")
    
    # Example 3: Get specific subsection
    print("\n3. 获取特定小节（例如：2a 方法流程）：")
    print("-" * 80)
    subsection_2a = analyzer.get_analysis_prompt("2", "a")
    print(subsection_2a + "\n")
    
    # Example 4: Generate template
    print("\n4. 生成论文分析模板：")
    print("-" * 80)
    template = analyzer.generate_analysis_template("示例论文：Attention Is All You Need")
    print(template[:400] + "...\n")
    
    print("\n" + "=" * 80)
    print("系统功能说明：")
    print("- get_full_framework(): 获取完整的分析框架")
    print("- get_analysis_prompt(section, subsection): 获取特定章节的分析提示")
    print("- generate_analysis_template(paper_title): 生成可填写的分析模板")
    print("=" * 80)


if __name__ == "__main__":
    main()
