from abc import ABC, abstractmethod

from domain.data import TemplateTrainData
from domain.model import Model


class ModelRepository(ABC):
    """データベースとの連携を担うクラス"""

    @abstractmethod
    def load(self) -> Model:
        pass


class DataRepository(ABC):
    @abstractmethod
    def load(self) -> TemplateTrainData:
        pass
