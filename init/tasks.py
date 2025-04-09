import logging
import random
import tempfile
import qrcode


from celery import shared_task
from decimal import Decimal
from django.db.models import F
from django.core.mail import EmailMessage
from django.conf import settings

from init.models import SupplyChainNode

logger = logging.getLogger(__name__)


@shared_task
def check_celery_task():
    logger.info('Тестовая задача Celery отработала')
    return '********** check_celery_task **********'


@shared_task
def check_celery_beat_task():
    logger.info('Периодическая задача Celery Beat отработала')
    return '!!!!!!!!!! check_celery_beat_task !!!!!!!!!!'


@shared_task
def increase_debt():
    amount = Decimal(random.randint(5, 500))
    updated_count = SupplyChainNode.objects.all().update(debt=F('debt') + amount)
    logger.info(f'Увеличено на {amount} для {updated_count} звеньев')
    return f'Increased debt by {amount} for {updated_count} nodes'


@shared_task
def decrease_debt():
    amount = Decimal(random.randint(100, 10000))
    nodes = SupplyChainNode.objects.all()
    count = 0
    for node in nodes:
        if node.debt > 0:
            node.debt = max(Decimal(0), node.debt - amount)
            node.save()
            count += 1
    logger.info(f'Уменьшено на {amount} для {count} звеньев')
    return f'Decreased debt by {amount} for {count} nodes'


@shared_task
def clear_debt_task(ids):
    nodes = SupplyChainNode.objects.filter(id__in=ids)
    for node in nodes:
        node.debt = 0
        node.save()
    logger.info(f'Задолженность обнулена {nodes.count()} звеньев')
    return f'Debt cleared {nodes.count()} nodes'


@shared_task
def send_qr_code_email(node_id, user_email):
    try:
        node = SupplyChainNode.objects.select_related('address').get(id=node_id)
    except SupplyChainNode.DoesNotExist:
        return f'Node with id {node_id} not found'

    contact_data = (
        f'Название: {node.name}\n'
        f'Email: {node.email}\n'
        f'Адрес: {node.address}'
    )

    qr = qrcode.make(contact_data)
    with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as tmp_file:
        qr.save(tmp_file)
        tmp_file_path = tmp_file.name

    email = EmailMessage(
        subject='Контактные данные объекта (сети)',
        body='QR код с контактной информацией',
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=[user_email],
    )
    email.attach_file(tmp_file_path)
    email.send()

    return f'QR код отправлен на {user_email}'
