import hashlib
import hmac
from datetime import datetime

from django.conf import settings


def create_sha256_signature(user: str) -> str:
    """Create a sha256 signature for the given user."""
    user = user.encode()

    # Create bytes from key & time stamp
    byte_key = bytes(settings.SECRET_KEY + str(datetime.today().timestamp()), "UTF-8")

    # Create the signature using HMAC-SHA256
    signature = hmac.new(byte_key, user, hashlib.sha256).hexdigest().strip()

    return signature
