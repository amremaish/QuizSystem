import httplib2
from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail


@shared_task
def async_http_request(url, method, headers, json_body):
    response = httplib2.Http().request(
        url,
        method=method,
        headers=headers,
        body=json_body
    )[0]
    print(f'response code {response.status}')
    return response.status


@shared_task
def async_send_mail(email_to_list, title, body):
    send_mail(title, body, settings.EMAIL_HOST_USER,
              email_to_list,
              fail_silently=True,
              )
