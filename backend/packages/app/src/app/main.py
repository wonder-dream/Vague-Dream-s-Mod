from fastapi import FastAPI

from app.plugins import discover_plugins
from core.database import init_engine
from core.plugins.registry import PluginRegistry

async def lifespan(app: FastAPI):

    init_engine()

    global registry
    registry = PluginRegistry()
    plugin_list = discover_plugins()

    for plugin in plugin_list:
        await registry.register(plugin)
        app.include_router(plugin.router)

    await registry.startup_all()

    yield

    await registry.shutdown_all()

app = FastAPI(lifespan=lifespan)