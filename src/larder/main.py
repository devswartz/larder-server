"""FastAPI application factory."""

from __future__ import annotations

from fastapi import FastAPI

from larder import __version__
from larder.api import (
    auth,
    capabilities,
    health,
    households,
    imports,
    meal_plan,
    recipes,
    shopping,
    sync,
)
from larder.config import Settings, get_settings


def create_app(settings: Settings | None = None) -> FastAPI:
    app_name = (settings or get_settings()).app_name
    app = FastAPI(
        title=f"{app_name} Server",
        version=__version__,
        license_info={"name": "AGPL-3.0", "identifier": "AGPL-3.0-only"},
    )
    if settings is not None:
        app.dependency_overrides[get_settings] = lambda: settings
    app.include_router(health.router)
    app.include_router(capabilities.router, prefix="/v1")
    app.include_router(auth.router, prefix="/v1")
    app.include_router(households.router, prefix="/v1")
    app.include_router(sync.router, prefix="/v1")
    app.include_router(imports.router, prefix="/v1")
    app.include_router(recipes.router, prefix="/v1")
    app.include_router(meal_plan.router, prefix="/v1")
    shopping.register(app, prefix="/v1")
    return app


app = create_app()
