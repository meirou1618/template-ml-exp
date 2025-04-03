from datetime import datetime
from typing import Optional
from uuid import uuid4

from domain.model import Model


class Experiment:
    """実験を管理するアグリゲートルート"""

    def __init__(self, model: Model, created_by: Optional[str] = None):
        self.id = str(uuid4())
        self.model = model
        self.created_by = created_by
        self.created_at = datetime.now()
        self.training_data_summary = None

    def mark_trained(self):
        self.model.trained_at = datetime.now()
