from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Any


@dataclass(slots=True)
class DiscoveryResult:
    business_name: str

    website: str = ""
    domain: str = ""

    category: str = ""

    country: str = ""
    city: str = ""
    address: str = ""

    public_email: str = ""
    public_phone: str = ""

    source_name: str = ""
    source_url: str = ""

    metadata: dict[str, Any] = field(
        default_factory=dict
    )


class SourceAdapter(ABC):
    source_name = "base"

    @abstractmethod
    def discover(
        self,
        *,
        niche: str,
        location: str = "",
        keywords: list[str] | None = None,
        limit: int = 100,
    ) -> list[DiscoveryResult]:
        """
        Discover publicly available business leads.

        Every adapter must return normalized DiscoveryResult objects.
        """
        raise NotImplementedError