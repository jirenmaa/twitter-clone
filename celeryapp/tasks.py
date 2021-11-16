from celeryapp.artisan import app as artisan
from celeryapp.workers.mailer import email_activation_link, email_resetpassword_link


@artisan.task(name="send_email_activation")
def send_email_activation(recepients: list, hashkey: str, **kwargs):
    """Send activation link to user email"""
    email_activation_link(recepients, hashkey, **kwargs)


@artisan.task(name="send_email_resetpassword")
def send_email_resetpassword(recepients: list, hashkey: str, **kwargs):
    """Send resetpassword link to user email"""
    email_resetpassword_link(recepients, hashkey, **kwargs)
