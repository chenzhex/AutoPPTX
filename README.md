# AutoPPTX

![alt text](https://raw.githubusercontent.com/chenzhex/AutoPPTX/main/assets/image.png)

**AutoPPTX** is a Python toolkit for automated editing of PowerPoint templates using the [`python-pptx`](https://python-pptx.readthedocs.io/) library.  
It is designed for data scientists, researchers, and business analysts who want to automate slide generation from structured data such as JSON files.  
> AutoPPTX supports intelligent replacement and styling of text, image, and table placeholders in PowerPoint templates.

---

## Features

- ✅ **Multi-type placeholder replacement**  
  Replace titles, subtitles, body text, images, and tables with structured data.

- 🎨 **Styling Support**  
  Supports style extraction, style application, and style transfer across text boxes, tables, and images — including font, alignment, background color, position, size...

- 🔍 **Placeholder type recognition and content inspection**  
  Identify and inspect placeholder types (text, image, table) and their content.

- 🧩 **Modular architecture**  
  Well-structured codebase with separate modules for Text, Image, Table, Type, and View.

- 🧪 **Tested and standardized**  
  Includes unit tests and conforms to [PEP8](https://peps.python.org/pep-0008/) and [black](https://black.readthedocs.io/en/stable/) code formatting.

---

## 📽️ Demo Preview

The following animation demonstrates how AutoPPTX replaces placeholders and styles text, images, and tables based on JSON input:

![AutoPPTX Demo](https://raw.githubusercontent.com/chenzhex/AutoPPTX/main/assets/autopptx_demo.gif)

---

## Requirements

- Python >= 3.10  
- `python-pptx` >= 1.0.2  
- `lxml` >= 5.3.1  

---

## Installation

```bash
# For regular usage
pip install autopptx

# For development (includes test dependencies)
pip install -e ".[dev]"
```

---

## Usage

### CLI Example

```bash
python -m autopptx.core.runner \
    --template ./data/template.pptx \
    --input ./data/input_data.json \
    --output ./data/output_demo.pptx
```

### Python API Example

```python
from autopptx.core.runner import main

main(
    template_path="./data/template.pptx",
    input_json="./data/input_data.json",
    output_path="./data/output_demo.pptx",
)
```

### Example Input (`input_data.json`)

```json
[
  {
    "title": "What They Eat",
    "subtitle": "Table 1",
    "bodytext": "Cats need protein-rich diets, primarily consisting of meat.",
    "table": [
      [
        ["Animal", "Favorite Food"],
        ["Cat", "Fish, Meat"],
        ["Bunny", "Carrots, Hay"]
      ]
    ]
  }
]
```

---

## Project Structure

```
AutoPPTX/
├── autopptx/             # 📦 Main Python package
│   ├── Text/             # Text replacement & style
│   ├── Image/            # Image replacement & layout
│   ├── Table/            # Table replacement & formatting
│   ├── Type/             # Placeholder type detection
│   ├── View/             # Slide viewer tools
│   └── core/             # CLI runner entry point
├── data/                 # Example JSON and PPTX templates
├── assets/               # README media (GIFs, images)
├── tests/                # Unit tests
├── env.sh                # Environment setup script
├── pyproject.toml        # Build & packaging configuration
├── MANIFEST.in           # Packaging resource includes
├── requirements.txt      # Python dependencies list
├── .gitignore            # Git ignore rules
├── LICENSE               # MIT License
└── README.md             # Project documentation
```

---

## Development

Clone the repo and set up:

```bash
git clone https://github.com/chenzhex/AutoPPTX.git
cd AutoPPTX
pip install -e ".[dev]"
```

### Code Formatting

```bash
black autopptx tests
```

### Running Tests

```bash
pytest tests/ --cov=autopptx
```

---

## Contributing

Contributions, issues, and feature requests are welcome!  
Please open a GitHub Issue or submit a Pull Request.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Citation

If you use **AutoPPTX** in your research, please cite the following JOSS paper:

```bibtex
@article{chen2025autopptx,
  title   = {AutoPPTX: Automated PowerPoint Generation with Python},
  author  = {Chen, Zhe},
  journal = {Journal of Open Source Software},
  year    = {2025},
  note    = {Submitted}
}
```

---

*AutoPPTX simplifies and streamlines automated slide generation for reproducible research and business reporting.*