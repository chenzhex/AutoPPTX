# AutoPPTX package metadata
__version__ = "0.1.2"
__author__ = "chenzhe"
__email__ = "chenzhe0_0@163.com"
__license__ = "MIT"
__url__ = "https://github.com/chenzhex/AutoPPTX"
__description__ = "Automated PowerPoint template editing toolkit based on python-pptx."

# ───────────────────────────────
# Text module
# ───────────────────────────────
from .Text.text import replace_bodytext
from .Text.texts import replace_title, replace_subtitle, replace_bodytexts
from .Text.style import (
    set_paragraph_style,
    set_textbox_style,
    extract_paragraph_style,
    extract_textbox_style,
)

# ───────────────────────────────
# Image module
# ───────────────────────────────
from .Image.image import replace_image
from .Image.images import replace_images
from .Image.style import (
    set_image_style,
    extract_image_style,
    transfer_image_style,
)

# ───────────────────────────────
# Table module
# ───────────────────────────────
from .Table.table import (
    insert_table,
    replace_table,
    replace_table_cell,
    validate_single_table,
)
from .Table.tables import replace_tables, validate_table_data
from .Table.style import (
    set_table_cell,
    set_table_style,
    extract_cell_style,
    extract_table_style,
    transfer_table_style,
)

# ───────────────────────────────
# Type module
# ───────────────────────────────
from .Type.find import find_placeholders
from .Type.type import (
    is_text,
    is_title,
    is_subtitle,
    is_bodytext,
    is_table,
    is_image,
)

# ───────────────────────────────
# View module
# ───────────────────────────────
from .View.view import get_text, get_table, get_image, view_slide

# ───────────────────────────────
# Exported API
# ───────────────────────────────
__all__ = [
    # Text
    "replace_bodytext",
    "replace_title",
    "replace_subtitle",
    "replace_bodytexts",
    "set_paragraph_style",
    "set_textbox_style",
    "extract_paragraph_style",
    "extract_textbox_style",
    # Image
    "replace_image",
    "replace_images",
    "set_image_style",
    "extract_image_style",
    "transfer_image_style",
    # Table
    "insert_table",
    "replace_table",
    "replace_table_cell",
    "validate_single_table",
    "replace_tables",
    "validate_table_data",
    "set_table_cell",
    "set_table_style",
    "extract_cell_style",
    "extract_table_style",
    "transfer_table_style",
    # Type
    "find_placeholders",
    "is_text",
    "is_title",
    "is_subtitle",
    "is_bodytext",
    "is_table",
    "is_image",
    # View
    "get_text",
    "get_table",
    "get_image",
    "view_slide",
]