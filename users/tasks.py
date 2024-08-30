from goodreads.celery import app
from django.core.mail import send_mail

@app.task()
def send_mail(subject, message, recipient_list):
    send_mail(
        subject,
        message,
        "wewolfuz@gmail.com",
        recipient_list
    )
