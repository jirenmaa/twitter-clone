from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Tweet, ResponseLike


def trigger():
    """An empty method to trigger the signals"""
    pass


@receiver(post_save, sender=Tweet)
def create_tweet(sender, instance, created, **kwargs):
    """
    Each time use create a tweet it will also create response like instead of
    using `Integer` field in tweet model.

    So everytime use like some tweet, the model will append the user using
    .add() method, so it can track who is like your tweet (especially your
    follower or your following)
    """
    if created:
        ResponseLike.objects.create(tweet=instance)
