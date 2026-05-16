class CoreException(Exception):

    def __init__(self, message: str, detail: dict | None = None):
        super().__init__(message)
        self.message = message
        self.detail = detail or {}

class PluginException(CoreException):
    def __init__(self, message: str, plugin_name: str, detail: dict | None = None):
        super().__init__(message, detail)
        self.plugin_name = plugin_name

class PluginNotFoundException(PluginException):
    def __init__(self, plugin_name: str, detail: dict | None = None):
        super().__init__(f"Plugin {plugin_name} not found", plugin_name, detail)

class PluginInitError(PluginException):
    def __init__(self, plugin_name: str, detail: dict | None = None):
        super().__init__(f"Plugin {plugin_name} init error", plugin_name, detail)

class PluginAlreadyExistsException(PluginException):
    def __init__(self, plugin_name: str, detail: dict | None = None):
        super().__init__(f"Plugin {plugin_name} already exists", plugin_name, detail)
