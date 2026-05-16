from abc import abstractmethod

from fastapi import APIRouter

from core.plugins.base import BasePlugin


class ToolkitPlugin(BasePlugin):
    @property
    @abstractmethod
    def display_name(self) -> str:
        pass

    router: APIRouter

    def get_agent_tools(self) -> None:
        pass