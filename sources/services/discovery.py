from collections.abc import Iterable

from sources.adapters.base import DiscoveryResult
from sources.adapters.registry import SourceRegistry


class DiscoveryService:
    def __init__(
        self,
        registry: SourceRegistry,
    ):
        self.registry = registry

    def discover(
        self,
        *,
        source_names: Iterable[str],
        niche: str,
        location: str = "",
        keywords: list[str] | None = None,
        limit: int = 100,
    ) -> list[DiscoveryResult]:

        results: list[DiscoveryResult] = []

        remaining = limit

        for source_name in source_names:
            if remaining <= 0:
                break

            adapter = self.registry.get(
                source_name
            )

            source_results = adapter.discover(
                niche=niche,
                location=location,
                keywords=keywords,
                limit=remaining,
            )

            results.extend(source_results)

            remaining = limit - len(results)

        return results[:limit]