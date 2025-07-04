from .text import replace_bodytext
from .texts import replace_title, replace_subtitle, replace_bodytexts
from .style import (
    set_paragraph_style,
    set_textbox_style,
    extract_paragraph_style,
    extract_textbox_style,
)

__all__ = [
    "replace_title",
    "replace_subtitle",
    "replace_bodytexts",
    "replace_bodytext",
    "set_paragraph_style",
    "set_textbox_style",
    "extract_paragraph_style",
    "extract_textbox_style",
]