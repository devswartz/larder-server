"""PowerSync write path: the table registry and the upload applier."""

from larder.sync import tables as _default_tables  # noqa: F401 - registers built-in tables
from larder.sync.registry import (
    SyncTable,
    WriteContext,
    WriteRejected,
    get_table,
    register,
    registered_tables,
)

__all__ = [
    "SyncTable",
    "WriteContext",
    "WriteRejected",
    "get_table",
    "register",
    "registered_tables",
]
