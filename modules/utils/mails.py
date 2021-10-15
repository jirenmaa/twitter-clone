from django.core.mail import send_mail


def activate_email_account(scheme, host, recipient, link_activation):
    """
    Send an email to the user with the activation link.
    """

    subject = "Activate your account"
    link_activation = f"{scheme}://{host}/auth/activate/?key={link_activation}"

    message = f"""Hey, {recipient}!,\nClick on the following link to activate your tweetter account {link_activation}
    """

    send_mail(
        subject=subject,
        message=message,
        from_email="Tweetter <noreply@tweetter.herokuapp>",
        recipient_list=[recipient],
        fail_silently=False,
    )

def reset_password_account(scheme, host, recipient, link_reset_password):
    """
    Send an email to the user with the reset password link.
    """

    subject = "Reset your password"
    link_reset_password = f"{scheme}://{host}/auth/reset_password/?key={link_reset_password}"

    message = f"""Hey, {recipient}!,\nClick on the following link to reset your password {link_reset_password}
    """

    send_mail(
        subject=subject,
        message=message,
        from_email="Tweetter <noreply@tweetter.herokuapp>",
        recipient_list=[recipient],
        fail_silently=False,
    )