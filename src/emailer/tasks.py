from celery import shared_task
from django.core.mail import send_mail
from celery.utils.log import get_task_logger
from smtplib import SMTPException


logger = get_task_logger(__name__)

@shared_task
def mail_send(
    subject, 
    message, 
    from_email, 
    recipient_list, 
    fail_silently=False) -> None:

    try:
        send_mail(
            subject=subject,
            message=message,
            from_email=from_email,
            recipient_list=recipient_list,
            fail_silently=fail_silently
        )
        logger.info(f"EMAIL SENT SUCESSFULLY TO {recipient_list[0]}")
    except SMTPException as e:
        logger.error(f"EMAIL SEND FAILED TO {recipient_list[0]}")