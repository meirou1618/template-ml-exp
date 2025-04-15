from __future__ import annotations

import numpy as np

from domain.ml_model import MLModel


class TemplateMLModel(MLModel):
    def __init__(self, model):
        super().__init__(model)

    def fit(self, data) -> MLModel:
        fitted = self._model.fit(data)  # 利用するモデルごとに変化する
        return TemplateMLModel(fitted)

    def predict(self, data) -> np.ndarray:
        return self._model.predict(data)
