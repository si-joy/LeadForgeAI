import ipaddress
import socket
from urllib.parse import urlparse


class UnsafeURL(ValueError):
    pass


ALLOWED_SCHEMES = {
    "http",
    "https",
}


def validate_public_url(url: str) -> str:
    parsed = urlparse(url)

    if parsed.scheme not in ALLOWED_SCHEMES:
        raise UnsafeURL(
            "Only HTTP and HTTPS URLs are allowed."
        )

    if not parsed.hostname:
        raise UnsafeURL(
            "URL must include a valid hostname."
        )

    hostname = parsed.hostname.lower().strip()

    if hostname in {
        "localhost",
        "localhost.localdomain",
    }:
        raise UnsafeURL(
            "Localhost URLs are not allowed."
        )

    try:
        addresses = socket.getaddrinfo(
            hostname,
            parsed.port or 443,
            type=socket.SOCK_STREAM,
        )
    except socket.gaierror as exc:
        raise UnsafeURL(
            "Hostname could not be resolved."
        ) from exc

    for address in addresses:
        ip_string = address[4][0]

        try:
            ip = ipaddress.ip_address(ip_string)
        except ValueError:
            continue

        if (
            ip.is_private
            or ip.is_loopback
            or ip.is_link_local
            or ip.is_multicast
            or ip.is_reserved
            or ip.is_unspecified
        ):
            raise UnsafeURL(
                "Private or internal network addresses are not allowed."
            )

    return url