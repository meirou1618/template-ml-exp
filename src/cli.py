import logging
import logging.config

import click

from aplication.aplication_service import AplicationServiceHandler
from aplication.template_service import TemplateService
from infrastructure.template_repository import (
    TemplateDataRepository,
    TemplateModelRepository,
)

logger = logging.getLogger()

logger.setLevel(logging.INFO)

ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
ch.setFormatter(formatter)
logger.addHandler(ch)


@click.group
def cli():
    """コマンドグループ
    @cliのデコレータでコマンドを管理
    """
    pass


@cli.command()
def template_command():
    # サービスの読み込み
    service = TemplateService(
        model_repo=TemplateModelRepository(),
        data_repo=TemplateDataRepository(
            X_path="temp_X_path", y_path="temp_y_path"
        ),
    )
    # サービスの実行
    AplicationServiceHandler.handle(service=service)


@cli.command()
def train():
    """trainコマンド（テンプレのため関数名変更可能）"""
    pass


@cli.command()
def exp():
    """experimentコマンド（テンプレのため関数名変更可能）"""
    pass


if __name__ == "__main__":
    cli()
