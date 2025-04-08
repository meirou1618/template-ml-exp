from abc import ABC, abstractmethod

import pandas as pd

from domain.data import TemplateData
from domain.ml_model import TemplateMLModel
from domain.model import Model, TemplateModel


class ModelRepository(ABC):
    """データベースとの連携を担うクラス"""

    @abstractmethod
    def load(self) -> Model:
        pass


class TemplateModelRepository(ModelRepository):
    def __init__(self) -> None:
        super().__init__()

    def load(self) -> Model:
        model = TemplateModel(
            id="test",
            params=dict(),
            ml_model=TemplateMLModel(model="ここに扱うモデルを渡す"),
        )

        return model


class DataRepository(ABC):
    @abstractmethod
    def load(self) -> TemplateData:
        pass


class TemplateDataRepository(DataRepository):
    def __init__(self, X_path: str, y_path: str) -> None:
        self.X_path = X_path
        self.y_path = y_path

    def load(self) -> TemplateData:
        X = pd.read_csv(self.X_path)
        y = pd.read_csv(self.y_path)
        return TemplateData(X=X, y=y)
