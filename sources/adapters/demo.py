from .base import DiscoveryResult, SourceAdapter


class DemoSourceAdapter(SourceAdapter):
    source_name = "demo"

    def discover(
        self,
        *,
        niche: str,
        location: str = "",
        keywords: list[str] | None = None,
        limit: int = 100,
    ) -> list[DiscoveryResult]:

        sample_results = [
            DiscoveryResult(
                business_name="Northstar Studio",
                website="https://example.com",
                domain="example.com",
                category=niche,
                city=location,
                source_name=self.source_name,
                source_url="https://example.com",
                metadata={
                    "keywords": keywords or [],
                },
            )
        ]

        return sample_results[:limit]