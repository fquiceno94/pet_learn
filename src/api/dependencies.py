from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from src.infrastructure.polymarket.gamma_client import GammaClient
from src.infrastructure.database.repositories import PostgresMarketRepository
from src.application.markets.ingest_markets import IngestMarketsUseCase
from src.infrastructure.database.session import get_session

async def get_ingest_use_case(session: AsyncSession= Depends(get_session)):
    gamma_client = GammaClient()
    postgres_repository = PostgresMarketRepository(session=session)

    use_case = IngestMarketsUseCase(gamma_client, postgres_repository)

    return use_case