from dataclasses import dataclass

@dataclass
class Market:
    id: str
    question: str
    outcome_prices: list[str]
    volume: float
    liquidity: float
    active: bool
    closed: bool

    def __post_init__(self):
        if not isinstance(self.volume, float):
            raise TypeError("volume debe ser float")
        if not isinstance(self.liquidity, float):
            raise TypeError("liquidity debe ser float")
        if not isinstance(self.active, bool):
            raise TypeError("active debe ser bool")
        if not isinstance(self.closed, bool):
            raise TypeError("closed debe ser bool")
