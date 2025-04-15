import logging
from typing import Protocol

logger = logging.getLogger(__name__)


class AplicationService(Protocol):
    """アプリケーションサービスの抽象クラス"""

    def handle(self):
        pass


class AplicationServiceHandler:
    """アプリケーションサービスの実行クラス"""

    @staticmethod
    def handle(service: AplicationService):
        try:
            logger.debug(f"Run: {service}")
            service.handle()
        except Exception as e:
            logger.error(e)
