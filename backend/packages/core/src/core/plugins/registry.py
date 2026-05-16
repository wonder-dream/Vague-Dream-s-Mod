from core.exceptions import PluginAlreadyExistsException, PluginInitError
from core.plugins.base import BasePlugin
from core.exceptions import PluginNotFoundException


class PluginRegistry:
    def __init__(self):
        self._plugins = {}

    async def register(self, plugin: BasePlugin) -> None:
        """将 plugin 注册到注册表中
        Args:
            plugin: 要注册进注册表的 plugin 对象
        """
        if plugin.name in self._plugins:
            raise PluginAlreadyExistsException(plugin.name)

        try:
            await plugin.on_init()
        except Exception as e:
            raise PluginInitError(plugin.name) from e

        plugin.is_initialized = True
        self._plugins[plugin.name] = plugin

    def get(self, name:str) -> BasePlugin:
        if name not in self._plugins:
            raise PluginNotFoundException(name)
        return self._plugins[name]

    def list_all(self) -> list[BasePlugin]:
        return list(self._plugins.values())

    def list_running(self) -> list[BasePlugin]:
        return list(p for p in self._plugins.values() if p.is_running)

    async def startup_all(self) -> None:
        for plugin in self.list_all():
            await plugin.on_startup()
            plugin.is_running = True

    async def shutdown_all(self) -> None:
        for plugin in reversed(list(self._plugins.values())):
            await plugin.on_shutdown()
            plugin.is_running = False

