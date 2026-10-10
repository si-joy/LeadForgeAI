from urllib.parse import urlparse


def normalize_domain(url: str) -> str:
    if not url:
        return ""

    parsed = urlparse(url)

    hostname = parsed.hostname or ""

    hostname = hostname.lower().strip()

    if hostname.startswith("www."):
        hostname = hostname[4:]

    return hostname