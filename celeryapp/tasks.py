from celeryapp.artisan import app as artisan
from celeryapp.workers import mailer


@artisan.task(name="send_email_activation")
def send_email_activation(recepients: str, hashkey: str, **kwargs):
    """Send activation link to user email"""
    mailer.email_activation_link(recepients, hashkey, **kwargs)


@artisan.task(name="send_email_resetpassword")
def send_email_resetpassword(recepients: str, hashkey: str, **kwargs):
    """Send resetpassword link to user email"""
    mailer.email_resetpassword_link(recepients, hashkey, **kwargs)
