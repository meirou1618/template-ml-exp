import logging

from domain.domain_services import ModelTrainer
from domain.experiment import Experiment
from infrastructure.template_repository import (
    DataRepository,
    ModelRepository,
)

logger = logging.getLogger(__name__)


class TemplateService:
    """モデルの学習や推論などの実行サービスを定義するクラス"""

    def __init__(
        self,
        model_repo: ModelRepository,
        data_repo: DataRepository,
    ) -> None:
        self.model_repo = model_repo
        self.data_repo = data_repo

    def handle(self) -> None:
        """実行関数
        基本的にはcli.pyからはhandleだけを実行する形にできると理想
        """
        logger.info("このクラスはテンプレートです")
        train_data = self.data_repo.load()
        model = self.model_repo.load()
        experiment = Experiment(model=model)
        ModelTrainer.train(experiment=experiment, train_data=train_data)
