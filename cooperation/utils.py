from django.core.mail import EmailMessage

from config import settings
from cooperation.models import Cooperation


def path_upload_file(instance: Cooperation, filename: str) -> str:
    return f'cooperation/{instance.company}/{filename}'


def send_email_cooperation(coop_object: Cooperation) -> None:

    # добавить поддержку кириллицы

    company = coop_object.company
    name = coop_object.name
    phone = coop_object.phone
    mail = coop_object.email
    subject = coop_object.subject
    text = coop_object.text

    email_subject = f'{subject}: заявка от {company}'
    email_body = f'{text}\n\n{name}\n{phone}\n{mail}'

    message = EmailMessage(
        subject=email_subject,
        body=email_body,
        from_email=settings.EMAIL_HOST_USER,
        to=(settings.EMAIL_HOST_USER,)
    )

    if coop_object.file:
        filename = coop_object.file.name.rsplit('/', 1)[-1]
        with coop_object.file.open('r') as f:
            file = f.read()
            message.attach(filename, file)

    message.send()
