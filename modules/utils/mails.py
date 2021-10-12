from django.core.mail import send_mail


def activate_email_account(scheme, host, recipient, link_activation):
    """
    Send an email to the user with the activation link.
    """

    subject = "Activate your account"
    link_activation = f"{scheme}://{host}/auth/activate/?key={link_activation}"

    message = f"""Hey, {recipient}!,\nClick on the following link to activate your tweatter account {link_activation}
    """

    send_mail(
        subject=subject,
        message=message,
        from_email="Tweatter <noreply@tweatter.herokuapp>",
        recipient_list=[recipient],
        fail_silently=False,
    )
