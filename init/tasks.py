import logging

from celery import shared_task

logger = logging.getLogger(__name__)


@shared_task
def check_celey_task():
    logger.info("Тестовая задача Celery отработала")
    return "check_celey_task OK"


@shared_task
def check_celey_beat_task():
    logger.info("Периодическая задача Celery Beat отработала")
    return "check_celey_beat_task OK"
