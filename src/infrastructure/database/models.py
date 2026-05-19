from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy import JSON

class Base(DeclarativeBase):
    pass

class MarketModel(Base):
    __tablename__ = "markets"

    id: Mapped[str] = mapped_column(primary_key=True)
    question: Mapped[str]
    outcome_prices: Mapped[list] = mapped_column(JSON)
    volume: Mapped[float]
    liquidity: Mapped[float]
    active: Mapped[bool]
    closed: Mapped[bool]
