from __future__ import annotations
from typing import Protocol

from src.domain.markets.entities import Market

class MarketRepository(Protocol):

    async def save(self,market: Market) -> None: ...