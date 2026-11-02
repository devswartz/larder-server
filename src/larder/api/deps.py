"""Shared request dependencies for the household-scoped REST routes.

Re-exports the auth dependencies under the names the shopping, store, trip and connector
routers use. `Household` is the signed-in member's explicitly chosen household (see
`larder.auth.deps.get_current_household`).
"""

from __future__ import annotations

from larder.auth.deps import (
    HOUSEHOLD_HEADER,
    CurrentHousehold,
    CurrentHouseholdDep,
    DbSession,
    get_current_household,
)
from larder.db.deps import get_db

Household = CurrentHouseholdDep

__all__ = [
    "HOUSEHOLD_HEADER",
    "CurrentHousehold",
    "DbSession",
    "Household",
    "get_current_household",
    "get_db",
]
