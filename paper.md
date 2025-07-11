---
title: "AutoPPTX: Automated editing of PowerPoint templates using Python for Educational and Teaching Purposes"
tags:
  - Python
  - PowerPoint
  - Automation
  - Education
  - Teaching
  - Template editing
  - Document generation
authors:
  - name: Zhe Chen
    orcid: 0009-0009-2178-8208
    corresponding: true
    affiliation: 1
    email: chenzhe0_0@163.com
affiliations:
  - name: Minzu University of China, Beijing, China
    index: 1
date: 11 July 2025
bibliography: paper.bib
---

# Summary

**AutoPPTX** is a Python package designed to automate the creation and styling of PowerPoint presentations from structured input data, tailored especially for educational and teaching environments. Built on top of the widely used [`python-pptx`](https://python-pptx.readthedocs.io/) library [@python-pptx], it offers a modular API to dynamically edit `.pptx` templates, facilitating rapid generation of instructional materials.

This package enables educators, trainers, and instructional designers to efficiently produce consistent, data-driven slide decks with minimal manual effort. By automating the replacement and styling of placeholders—text, images, and tables—AutoPPTX supports reproducible and scalable creation of teaching presentations and lecture materials.

# Statement of Need

PowerPoint (`.pptx`) remains the global standard for educational presentations across K–12, higher education, vocational training, and online learning. Its flexibility and visual richness make it ideal for lectures, flipped classrooms, tutorials, and asynchronous instruction. However, educators often spend substantial time manually formatting, duplicating, and customizing slides to reflect evolving course content, assessments, or feedback.

While tools like LaTeX Beamer offer automation for academic publishing, `.pptx` lacks a similarly accessible and open-source solution tailored to educational workflows.

**AutoPPTX** bridges this gap by providing a lightweight, modular, and reproducible Python toolkit that automates PowerPoint slide generation from structured inputs. It enhances efficiency and consistency in instructional content creation through:

- ✅ **Rapid content generation**  
  Automatically fills text, image, and table placeholders based on structured lesson data, enabling quick updates to lectures, handouts, or assignment overviews.

- 🎨 **Consistent visual styling**  
  Applies uniform fonts, alignments, colors, and layouts from template slides, supporting institutional branding and improving clarity across course materials.

- 🧩 **Seamless integration**  
  Offers both code-based and command-line interfaces to fit within diverse teaching pipelines—ranging from Jupyter notebooks to learning management systems.

- 🔁 **Reproducibility and collaboration**  
  Enables scalable slide generation with versioned inputs, facilitating reuse, cross-course consistency, and collaborative development of teaching assets.

- ♿ **Accessibility support**  
  Encourages the use of high-contrast styles, readable fonts, and consistent layouts, improving comprehension for learners with visual impairments or cognitive differences.

By reducing repetitive manual work and standardizing presentation design, AutoPPTX empowers educators and instructional designers to deliver accessible, high-quality educational content—whether for in-person classrooms, hybrid environments, or fully online platforms.

# Functionality

AutoPPTX offers a focused set of features designed to support the creation of high-quality educational slide content efficiently and consistently:

- **Multi-format placeholder replacement**  
  Automatically replaces text, image, and table placeholders within PowerPoint templates using structured input data—ideal for lesson plans, data visualizations, or instructional tables.

- **Template-driven style preservation**  
  Ensures that generated slides inherit font styles, alignments, and visual layouts from the original template, promoting visual consistency across courses and sessions.

- **Flexible input-output integration**  
  Compatible with both Python scripting and command-line workflows, allowing easy integration with teaching automation tools, course content repositories, or LMS pipelines.

- **Scalable and modular architecture**  
  Components are organized by function (text, image, table, layout), enabling educators or developers to adapt or extend the toolkit for specific pedagogical formats or departmental standards.

- **Accessible and standards-aligned output**  
  By supporting the use of readable fonts and high-contrast color schemes from templates, AutoPPTX facilitates the production of slides that meet accessibility and readability best practices.

Collectively, these features make AutoPPTX well-suited for use in a variety of educational contexts—from updating weekly lecture slides to batch-generating differentiated instructional materials or onboarding content.

# Installation

```bash
pip install autopptx
````

# Example Usage

## CLI

```bash
python -m autopptx.core.runner \
    --template ./data/template.pptx \
    --input ./data/input_data.json \
    --output ./data/output_demo.pptx
```

## Python API

```python
from autopptx.core.runner import main

main(
    template_path="./data/template.pptx",
    input_json="./data/input_data.json",
    output_path="./data/output_demo.pptx",
)
```

# Figures

AutoPPTX supports visualization of extracted content through utilities in the `View` module. Example teaching slides generated by AutoPPTX can be previewed in the [project repository](https://github.com/chenzhex/AutoPPTX#readme).

![Figure 1: Example teaching slide generated by AutoPPTX.](./assets/autopptx_demo.gif)

# Acknowledgements

This project builds upon the foundational work of `python-pptx` by Scanny and was inspired by the practical challenges faced by educators and trainers in preparing high-quality, data-driven presentations. The author appreciates feedback from early adopters and contributors.

# Availability

AutoPPTX is fully open-source and available at:

* **GitHub repository**: [https://github.com/chenzhex/AutoPPTX](https://github.com/chenzhex/AutoPPTX)
* **PyPI package**: [https://pypi.org/project/autopptx](https://pypi.org/project/autopptx)

# References