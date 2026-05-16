from abc import abstractmethod, ABC


class BasePlugin(ABC):

    # --- 身份 ---
    @property
    @abstractmethod
    def name(self) -> str:
        pass

    @property
    @abstractmethod
    def version(self) -> str:
        pass

    @property
    @abstractmethod
    def description(self) -> str:
        pass

    # --- 生命周期 ---
    async def on_init(self) -> None:
        pass

    async def on_startup(self) -> None:
        pass

    async def on_shutdown(self) -> None:
        pass

    # --- 状态 ---
    is_initialized: bool = False
    is_running: bool = False