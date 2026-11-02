"""All ORM models. Importing this package registers every table on `Base.metadata`."""

from larder.db.base import Base
from larder.models.auth import EmailLoginToken, HouseholdInvite, RefreshToken
from larder.models.catalog import Ingredient, IngredientAlias
from larder.models.connectors import ConnectorAccount, ConnectorItemLink
from larder.models.identity import Household, HouseholdMember, HouseholdRole, User
from larder.models.imports import ImportJob, ImportSourceKind, ImportStatus, LlmUsage
from larder.models.learning import LearningEvent, LlmCache
from larder.models.planning import MealPlanEntry, MealSlot
from larder.models.recipes import (
    ImportConfidence,
    Recipe,
    RecipeIngredient,
    RecipeSourceType,
    RecipeStep,
    RecipeTag,
    ReviewState,
    Tag,
)
from larder.models.shopping import (
    ItemSourceType,
    ItemStatus,
    ShoppingItem,
    ShoppingItemSource,
    ShoppingList,
    Trip,
    TripKind,
    TripStatus,
    Urgency,
)
from larder.models.stores import ItemStorePref, Store, StoreGroup, StoreGroupMember

__all__ = [
    "Base",
    "ConnectorAccount",
    "ConnectorItemLink",
    "EmailLoginToken",
    "Household",
    "HouseholdInvite",
    "HouseholdMember",
    "HouseholdRole",
    "ImportConfidence",
    "ImportJob",
    "ImportSourceKind",
    "ImportStatus",
    "Ingredient",
    "IngredientAlias",
    "ItemSourceType",
    "ItemStatus",
    "ItemStorePref",
    "LearningEvent",
    "LlmCache",
    "LlmUsage",
    "MealPlanEntry",
    "MealSlot",
    "Recipe",
    "RecipeIngredient",
    "RecipeSourceType",
    "RecipeStep",
    "RecipeTag",
    "RefreshToken",
    "ReviewState",
    "ShoppingItem",
    "ShoppingItemSource",
    "ShoppingList",
    "Store",
    "StoreGroup",
    "StoreGroupMember",
    "Tag",
    "Trip",
    "TripKind",
    "TripStatus",
    "Urgency",
    "User",
]
