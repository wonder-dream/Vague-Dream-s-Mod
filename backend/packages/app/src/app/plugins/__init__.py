import importlib
import inspect
import os
import pkgutil

from app.plugins.base import ToolkitPlugin


def discover_plugins() -> list:
    plugin_list = []

    for _, name, is_pkg in pkgutil.iter_modules([os.path.dirname(__file__)]):
        if not is_pkg:
            continue

        module = importlib.import_module(f"app.plugins.{name}.plugin")

        for _, obj in inspect.getmembers(module):
            if inspect.isclass(obj) and issubclass(obj, ToolkitPlugin) and obj != ToolkitPlugin:
                plugin = obj()
                plugin_list.append(plugin)

    return plugin_list