import binascii
import hashlib
import hmac
from datetime import datetime
from urllib.parse import quote_plus

from django.conf import settings


def create_sha256_signature(user):
    """
    Create a sha256 signature for the given user.
    """
    user = user.encode()

    # Create bytes from the secret key
    byte_key = bytes(settings.SECRET_KEY + str(datetime.today().timestamp()), "UTF-8")

    # Create the signature using HMAC-SHA256
    signature = hmac.new(byte_key, user, hashlib.sha256)

    # Return the base64 encoded signature
    encoded = binascii.b2a_base64(signature.digest(), newline=False).decode().strip()

    # escape the signature to secure url (+, /, =)
    return quote_plus(encoded)
