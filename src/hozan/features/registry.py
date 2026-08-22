from __future__ import annotations

from dataclasses import dataclass
from typing import Protocol


class Feature(Protocol):
    name: str

    def register(self, bot) -> None:
        ...


@dataclass(slots=True)
class FeatureRegistry:
    """Feature composition without feature-to-feature coupling."""

    _features: dict[str, Feature]

    def __init__(self) -> None:
        self._features = {}

    def add(self, feature: Feature) -> None:
        if feature.name in self._features:
            raise ValueError(f"feature already registered: {feature.name}")
        self._features[feature.name] = feature

    def register_all(self, bot) -> None:
        for feature in self._features.values():
            feature.register(bot)
