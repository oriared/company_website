from django.core.mail import send_mail

from config import settings


def path_upload_file(instance, filename):
    return f'cooperation/{instance.company}/{filename}'


def send_email_cooperation(form):
    data = form.cleaned_data
    company = data['company']
    print(f'email to {company} - OK')
    # subject = f'{data.subject} {data.company}'
    # content = f'{data.text}\n\n{data.person}\n{data.email}\n{data.phone}'
    # send_mail(subject, content,
    #           settings.EMAIL_HOST_USER,
    #           (settings.EMAIL_HOST_USER,))
