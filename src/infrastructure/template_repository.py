import pandas as pd

from domain.data import TemplateTrainData
from domain.model import Model, TemplateModel
from domain.repository import DataRepository, ModelRepository
from infrastructure.template_ml_model import TemplateMLModel


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


class TemplateDataRepository(DataRepository):
    def __init__(self, X_path: str, y_path: str) -> None:
        self.X_path = X_path
        self.y_path = y_path

    def load(self) -> TemplateTrainData:
        X = pd.read_csv(self.X_path)
        y = pd.read_csv(self.y_path)
        return TemplateTrainData(X=X, y=y)
