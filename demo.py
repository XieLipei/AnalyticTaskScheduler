#!/usr/bin/env python3
"""
Demo script for Academic Paper Methodology Analyzer
演示脚本：学术论文方法分析系统

This script demonstrates the main features of the paper analyzer.
此脚本演示论文分析器的主要功能。
"""

from paper_analyzer import PaperAnalyzer
import sys


def print_separator(char="=", length=80):
    """Print a separator line."""
    print(char * length)


def demo_basic_usage():
    """Demonstrate basic usage of the analyzer."""
    print_separator()
    print("示例 1: 基本使用 / Example 1: Basic Usage")
    print_separator()
    
    analyzer = PaperAnalyzer()
    
    print("\n1.1 获取完整分析框架 / Get full framework:")
    print("-" * 80)
    framework = analyzer.get_full_framework()
    # Print first 500 characters
    print(framework[:500] + "...\n")
    print(f"[完整框架长度: {len(framework)} 字符]")


def demo_section_query():
    """Demonstrate querying specific sections."""
    print("\n")
    print_separator()
    print("示例 2: 查询特定章节 / Example 2: Query Specific Section")
    print_separator()
    
    analyzer = PaperAnalyzer()
    
    print("\n2.1 查询'方法设计'章节 (Section 2):")
    print("-" * 80)
    section = analyzer.get_analysis_prompt("2")
    print(section)
    
    print("\n2.2 查询'方法流程'小节 (Section 2a):")
    print("-" * 80)
    subsection = analyzer.get_analysis_prompt("2", "a")
    print(subsection)


def demo_template_generation():
    """Demonstrate template generation."""
    print("\n")
    print_separator()
    print("示例 3: 生成分析模板 / Example 3: Generate Analysis Template")
    print_separator()
    
    analyzer = PaperAnalyzer()
    
    paper_title = "Vision Transformer (ViT)"
    print(f"\n为论文生成分析模板: {paper_title}")
    print("-" * 80)
    
    template = analyzer.generate_analysis_template(paper_title)
    
    # Save to file
    filename = f"{paper_title.replace(' ', '_')}_template.md"
    try:
        with open(filename, "w", encoding="utf-8") as f:
            f.write(template)
        print(f"✓ 模板已保存到: {filename}")
        print(f"✓ 模板长度: {len(template)} 字符")
        print(f"\n模板预览（前600字符）:")
        print("-" * 80)
        print(template[:600] + "...")
    except Exception as e:
        print(f"✗ 保存失败: {e}")


def demo_all_sections():
    """Demonstrate all available sections."""
    print("\n")
    print_separator()
    print("示例 4: 浏览所有章节 / Example 4: Browse All Sections")
    print_separator()
    
    analyzer = PaperAnalyzer()
    
    sections = [
        ("0", "摘要翻译 / Abstract Translation"),
        ("1", "方法动机 / Method Motivation"),
        ("2", "方法设计 / Method Design"),
        ("3", "方法对比 / Method Comparison"),
        ("4", "实验表现 / Experimental Performance"),
        ("5", "学习应用 / Learning & Application"),
        ("6", "总结 / Summary"),
    ]
    
    for num, title in sections:
        print(f"\n章节 {num}: {title}")
        print("-" * 80)
        content = analyzer.get_analysis_prompt(num)
        # Print first 200 characters of each section
        preview = content[:200].replace("\n\n", "\n")
        print(preview + "...")


def demo_interactive_mode():
    """Interactive mode for exploring the analyzer."""
    print("\n")
    print_separator()
    print("示例 5: 交互模式 / Example 5: Interactive Mode")
    print_separator()
    
    analyzer = PaperAnalyzer()
    
    print("\n进入交互模式。输入章节编号（0-6）查看详情，或输入 'q' 退出。")
    print("Enter section number (0-6) to view details, or 'q' to quit.\n")
    
    while True:
        try:
            user_input = input("请输入章节编号 / Enter section number: ").strip()
            
            if user_input.lower() in ['q', 'quit', 'exit']:
                print("退出交互模式 / Exiting interactive mode.")
                break
            
            if user_input in ['0', '1', '2', '3', '4', '5', '6']:
                print("\n" + "-" * 80)
                content = analyzer.get_analysis_prompt(user_input)
                print(content)
                print("-" * 80 + "\n")
            else:
                print(f"无效输入。请输入 0-6 之间的数字。/ Invalid input. Please enter 0-6.")
                
        except KeyboardInterrupt:
            print("\n\n退出交互模式 / Exiting interactive mode.")
            break
        except EOFError:
            print("\n\n退出交互模式 / Exiting interactive mode.")
            break


def main():
    """Main function to run all demos."""
    print("\n")
    print_separator("=", 80)
    print("学术论文方法分析系统 - 演示")
    print("Academic Paper Methodology Analyzer - Demo")
    print_separator("=", 80)
    
    # Run all demos
    demo_basic_usage()
    demo_section_query()
    demo_template_generation()
    demo_all_sections()
    
    # Ask if user wants interactive mode
    print("\n")
    print_separator("=", 80)
    try:
        response = input("\n是否进入交互模式？(y/n) / Enter interactive mode? (y/n): ").strip().lower()
        if response in ['y', 'yes']:
            demo_interactive_mode()
    except (KeyboardInterrupt, EOFError):
        print("\n")
    
    print("\n")
    print_separator("=", 80)
    print("演示完成！/ Demo completed!")
    print("请查看 README.md 和 USAGE_GUIDE.md 了解更多信息。")
    print("Please see README.md and USAGE_GUIDE.md for more information.")
    print_separator("=", 80)
    print("\n")


if __name__ == "__main__":
    main()
