import string
from random import choices

ascii_charset = string.ascii_letters + string.digits


def token_generator() -> str:
    return "".join(choices(ascii_charset, k=48))
