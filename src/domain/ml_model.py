from __future__ import annotations


class MLModel:
    """MLモデルの抽象クラス"""

    def __init__(self, model):
        self._model = model

    def fit(self, data) -> MLModel:
        return self

    def predict(self, data):
        pass
