import re
from uuid import uuid4

from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from django_bleach.models import BleachField

from modules.users.models import User


def tweet_tags_validator(value):
    """Tweet tags validator"""
    pattern = r"^([#A-Za-z\s]+)"
    message = _(
        "This value may contain only letters, underscore and white spaces characters"
    )
    regex_matches = re.fullmatch(pattern, str(value))
    if not regex_matches:
        raise ValidationError(message, code="invalid", params={"value": value})


class Tweet(models.Model):
    id = models.UUIDField(
        _("tweet id"), primary_key=True, default=uuid4, editable=False
    )
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tweets")
    pictures = models.ImageField(upload_to="pictures/", blank=True, null=True)
    tags = BleachField(
        _("tweet tags"),
        blank=True,
        max_length=100,
        help_text=_(
            "100 characters or fewer. Letters, underscore and white space only"
        ),
        validators=[tweet_tags_validator],
    )
    content = models.TextField(
        _("tweet content"),
        blank=True,
        max_length=264,
        help_text=_("264 characters maximal or fewer"),
    )
    created_at = models.DateTimeField(_("tweet created"), default=timezone.now)
    updated_at = models.DateTimeField(_("tweet updated"), default=timezone.now)

    def __str__(self):
        return str(self.id)


class ResponseLike(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    tweet = models.OneToOneField(Tweet, related_name="likes", on_delete=models.CASCADE)
    user = models.ManyToManyField(User, related_name="likes_users")
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.id)


class ResponseComment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    tweet = models.ForeignKey(Tweet, related_name="comments", on_delete=models.CASCADE)
    author = models.ForeignKey(
        User, null=True, related_name="commented_tweets", on_delete=models.CASCADE
    )
    pictures = models.ImageField(upload_to="pictures/", blank=True, null=True)
    content = models.TextField(
        _("comment content"),
        max_length=264,
        help_text=_("264 characters maximal or fewer"),
    )
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.id)

class ResponseUserLikedTweet(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE)
    author = models.ForeignKey(User, related_name="liked_tweet", on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.id)
