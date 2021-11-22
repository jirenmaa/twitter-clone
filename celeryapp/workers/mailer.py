from django.conf import settings
from django.core.mail import EmailMessage
from django.template.loader import get_template


def url_constructor(path: str, parameters: list, **kwargs) -> str:
    """return url"""
    scheme = kwargs.get("scheme", "http")
    host = kwargs.get("host", settings.WEBSITE_URL)

    # construct url
    general = "{0}://{1}/{2}".format(scheme, host, path)
    for parameter in parameters:
        general += "/{0}".format(parameter)

    return general


def generate_email_from_template(recipient: str, template: str, **kwargs) -> str:
    """return email render template"""
    signature = "?key={0}".format(kwargs.get("signature"))

    # context for template
    context = {
        "recepient": recipient,
        "url": url_constructor(path="activation", parameters=[signature], **kwargs),
    }
    return get_template("{0}.html".format(template)).render(context)


def email_activation_link(recipient: str, hash: str, **kwargs) -> None:
    """send email activation to recipeint email"""
    content = generate_email_from_template(
        recipient, "activation", signature=hash, **kwargs
    )
    # construct email message
    mailing = EmailMessage(
        subject="Account Activation",
        body=content,
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=[recipient],
    )
    mailing.content_subtype = "html"
    mailing.send()


def email_resetpassword_link(recipient: str, hash: str, **kwargs) -> None:
    """send email resetpassword to recipeint email"""
    content = generate_email_from_template(
        recipient, "resetpassword", signature=hash, **kwargs
    )
    # construct email message
    mailing = EmailMessage(
        subject="Reset Password",
        body=content,
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=[recipient],
    )
    mailing.content_subtype = "html"
    mailing.send()
