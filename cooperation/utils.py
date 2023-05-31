import os
from django.core.mail import EmailMessage
from django.db.models import Model
from django.forms import Form

from config import settings


def path_upload_file(instance: Model, filename: str) -> str:
    return f'cooperation/{instance.company}/{filename}'


def email_from_form(form: Form) -> None:

    # добавить поддержку кириллицы

    data = form.cleaned_data

    company = data['company']
    person = data['person']
    phone = data['phone']
    mail = data['email']
    subject = form.instance.subject
    text = data['text']

    email_subject = f'{subject}: заявка от {company}'
    email_body = f'{text}\n\n{person}\n{phone}\n{mail}'
    message = EmailMessage(
        subject=email_subject,
        body=email_body,
        from_email=settings.EMAIL_HOST_USER,
        to=(settings.EMAIL_HOST_USER,)
    )

    if data.get('file'):
        filename = data['file'].name.replace(' ', '_')
        file = os.path.join(settings.MEDIA_ROOT, 'cooperation',
                            company, filename)
        message.attach_file(file)

    message.send()
