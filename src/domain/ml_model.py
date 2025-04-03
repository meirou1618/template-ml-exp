from __future__ import annotations

import numpy as np


class MLModel:
    """MLモデルの値オブジェクト"""

    def __init__(self, model):
        self._model = model

    def fit(self, data) -> MLModel:
        return self

    def predict(self, data):
        pass


class TemplateMLModel(MLModel):
    def __init__(self, model):
        super().__init__(model)

    def fit(self, data) -> MLModel:
        fitted = self._model.fit(data)  # 利用するモデルごとに変化する
        return TemplateMLModel(fitted)

    def predict(self, data) -> np.ndarray:
        return self._model.predict(data)
