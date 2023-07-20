from celery import shared_task
from django.core.mail import send_mail


@shared_task
def notify_order_saved(order_pk, promocode):
    # from time import sleep
    # sleep(3)
    #
    send_mail(
        f"Order # {order_pk} saved",
        f"New order created: Order #: {order_pk}, promocode: {promocode}",
        'from@examlpe.com',
        ['to@example.com', 'you@your.yo'],
        fail_silently=True,
    )