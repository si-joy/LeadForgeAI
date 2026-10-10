from collections.abc import Iterable

from .base import SourceAdapter


class SourceRegistry:
    def __init__(self):
        self._adapters: dict[str, SourceAdapter] = {}

    def register(self, adapter: SourceAdapter) -> None:
        name = adapter.source_name.strip().lower()

        if not name:
            raise ValueError(
                "Source adapter must have a source_name."
            )

        if name in self._adapters:
            raise ValueError(
                f"Source adapter '{name}' is already registered."
            )

        self._adapters[name] = adapter

    def get(self, name: str) -> SourceAdapter:
        key = name.strip().lower()

        try:
            return self._adapters[key]
        except KeyError as exc:
            raise KeyError(
                f"Unknown source adapter: {name}"
            ) from exc

    def all(self) -> Iterable[SourceAdapter]:
        return self._adapters.values()

    def names(self) -> list[str]:
        return list(self._adapters.keys())