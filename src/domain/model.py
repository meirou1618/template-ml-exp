from abc import ABC
from datetime import datetime
from typing import Optional

from domain.ml_model import MLModel


class Model(ABC):
    """MLモデルを扱うエンティティ"""

    def __init__(
        self,
        id: str,
        params: dict,
        ml_model: MLModel,
        created_at: Optional[datetime] = None,
    ) -> None:
        self.id = id
        self.params = params
        if created_at:
            self.created_at = created_at
        else:
            self.created_at = datetime.now()
        self.ml_model = ml_model
        self.trained_at: Optional[datetime] = None

    def update_model(self, ml_model: MLModel):
        pass


class TemplateModel(Model):
    def __init__(
        self,
        id: str,
        params: dict,
        ml_model: MLModel,
        created_at: Optional[datetime] = None,
    ):
        super().__init__(id, params, ml_model, created_at)

    def update_model(self, ml_model: MLModel):
        self.ml_model = ml_model
        self.trained_at = datetime.now()
