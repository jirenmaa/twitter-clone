from django.core.mail import EmailMessage

from django.template.loader import get_template


def url_maker(scheme: str, host: str, path: str, parameters: list = None) -> str:
    general = "{0}://{1}/{2}".format(scheme, host, path)

    for parameter in parameters:
        general += "/{0}".format(parameter)

    return general


def email_activation_link(recipient: list, hash: str, **kwargs):
    """send email activation to recipeint email"""
    SCHEME = kwargs.get("scheme", "http")
    XHOSTS = kwargs.get("xhosts", "localhost:8080")
    HASHKEY = "?key={0}".format(hash)

    SUBJECT = "Account Activation"
    FROMAIL = "twitter clone <noreply@twitter-clone.com>"
    context = {
        "recepient": recipient,
        "activation_link": url_maker(SCHEME, XHOSTS, "activation", [HASHKEY])
    }

    content = get_template("account_activation.html").render(context)
    mailing = EmailMessage(SUBJECT, content, from_email=FROMAIL, to=[recipient])
    mailing.content_subtype = "html"
    mailing.send()


def email_resetpassword_link(recipient: list, hash: str, **kwargs):
    """send email resetpassword to recipeint email"""
    SCHEME = kwargs.get("SCHEME", "http")
    XHOSTS = kwargs.get("HOSTS", "localhost:8080")
    HASHKEY = "?key={0}".format(hash)

    SUBJECT = "Reset Password"
    FROMAIL = "twitter clone <noreply@twitter-clone.com>"
    context = {
        "recepient": recipient,
        "resetpassword_link": url_maker(SCHEME, XHOSTS, "resetpassword", [HASHKEY])
    }

    content = get_template("resetpassword.html").render(context)
    mailing = EmailMessage(SUBJECT, content, from_email=FROMAIL, to=[recipient])
    mailing.content_subtype = "html"
    mailing.send()
