import re
from bleach import linkify


def linkify_content(data: str) -> str:
    """Adding class to linkifed string
    :example: <a href="example.com" ...>example.com<a>
    :returns: <a href="example.com" ... class="...">example.com<a>
    """
    linkified = linkify(data)
    pattern = r"\srel=\"nofollow\">"
    replace = " rel=\"nofollow\" class=\"text-blue-600 leading-none\">"

    return re.sub(pattern, replace, linkified)
