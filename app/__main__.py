from litestar import Litestar
from litestar.openapi import OpenAPIConfig
from litestar.openapi.plugins import SwaggerRenderPlugin
from app.routes.offer_walls import router as offer_walls_router
from app.error_handler import register_exception_handlers

try:
    from app.config import settings
    APP_HOST = getattr(settings, "app_host", "0.0.0.0")
    APP_PORT = getattr(settings, "app_port", 5000)
except Exception:
    APP_HOST = "0.0.0.0"
    APP_PORT = 5000


openapi_config = OpenAPIConfig(
    title="TrafficMagnit API",
    version="1.0.0",
    description="Litestar мікросервіс, який дублює DRF API.",
    render_plugins=[SwaggerRenderPlugin()],  # генерує swagger UI
)


app = Litestar(
    route_handlers=[offer_walls_router],
    openapi_config=openapi_config,
)

register_exception_handlers(app)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "app.__main__:app",
        host=APP_HOST,
        port=APP_PORT,
        reload=True,
    )
