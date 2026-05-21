from sqlalchemy.ext.asyncio import AsyncSession

from src.domain.markets.entities import Market
from src.domain.markets.repositories import MarketRepository
from src.infrastructure.database.models import MarketModel

class PostgresMarketRepository(MarketRepository):

    def __init__(self, session: AsyncSession):
        self.session = session

    async def save(self, market: Market) -> None:
        
        # 1. convertir Market (dominio) → MarketModel (DB)
        model = MarketModel(
            id=market.id,
            question=market.question,
            outcome_prices=market.outcome_prices,
            volume=market.volume,
            liquidity=market.liquidity,
            active=market.active,
            closed=market.closed
        )     
        # Línea 2: upsert — si existe actualiza, si no inserta
        await self.session.merge(model)

        # Línea 3: guardar en DB
        await self.session.commit()

