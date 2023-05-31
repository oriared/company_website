import csv
import io

from django.core.mail import EmailMessage

from config import settings


def send_order_email(order):
    buffer = io.StringIO()
    writer = csv.writer(buffer)
    for item in order.items.all():
        writer.writerow((item.product_sku.sku, item.quantity))
    content = buffer.getvalue()
    buffer.close()
    email_subject = f'Заказ от {order.user.username}'
    email_body = f'Комментарий к заказу: {order.comment}'
    filename = f'{order.user.username}_order№{order.pk}.csv'
    mimetype = 'text/csv'
    message = EmailMessage(
        subject=email_subject,
        body=email_body,
        attachments=[(filename, content, mimetype)],
        from_email=settings.EMAIL_HOST_USER,
        to=(settings.EMAIL_HOST_USER,)
    )
    message.send()
