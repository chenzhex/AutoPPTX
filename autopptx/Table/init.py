from .table import (
    insert_table,
    replace_table,
    replace_table_cell,
    validate_single_table,
)
from .tables import replace_tables, validate_table_data
from .style import (
    set_table_cell,
    set_table_style,
    extract_cell_style,
    extract_table_style,
    transfer_table_style,
)

__all__ = [
    "insert_table",
    "replace_table",
    "replace_table_cell",
    "replace_tables",
    "validate_single_table",
    "validate_table_data",
    "set_table_cell",
    "set_table_style",
    "extract_cell_style",
    "extract_table_style",
    "transfer_table_style",
]