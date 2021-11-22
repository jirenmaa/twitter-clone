import re
from uuid import uuid4

from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.core.exceptions import ValidationError
from django.db.models import CharField, EmailField, ImageField, UUIDField, BooleanField
from django.utils.translation import gettext_lazy as _


def no_unicode_name_validator(value):
    """Validate that the input contains a match for the regular expression."""
    pattern = r"^([\w\s]+)"
    message = _(
        "Enter a valid Name. This value may contain only letters, "
        "white spaces, and characters."
    )
    regex_matches = re.fullmatch(pattern, str(value))
    if not regex_matches:
        raise ValidationError(message, code="invalid", params={"value": value})


class User(AbstractUser):
    username_validator = UnicodeUsernameValidator()

    id = UUIDField(primary_key=True, default=uuid4, editable=False)
    name = CharField(
        _("name"),
        max_length=50,
        help_text=_("Required. 50 characters or fewer. Letters, and white space only."),
        validators=[no_unicode_name_validator],
    )
    username = CharField(
        _("username"),
        max_length=15,
        unique=True,
        help_text=_("Required. 15 characters or fewer. Letters, digits and /-/_ only."),
        validators=[username_validator],
        error_messages={
            "unique": _("A user with that username already exists."),
        },
    )
    email = EmailField(_("email address"), max_length=35, unique=True, blank=False)
    avatar = ImageField(
        upload_to="avatars/",
        blank=True,
        null=True,
    )
    is_active = BooleanField(
        _("active"),
        default=False,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )

    # change the required `username` field to `email` since
    # django by default uses `username` as a required field.
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["password"]
