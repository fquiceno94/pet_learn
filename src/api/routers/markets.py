from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.infrastructure.database.session import get_session
from src.infrastructure.database.models import MarketModel
from src.api.dependencies import get_ingest_use_case
from src.application.markets.ingest_markets import IngestMarketsUseCase

class MarketResponse(BaseModel):
    id: str
    question: str
    outcome_prices: list[str]
    volume: float
    liquidity: float
    active: bool
    closed: bool

router = APIRouter(prefix="/markets", tags=["markets"])

@router.get("/", response_model=list[MarketResponse])
async def markets(session: AsyncSession = Depends(get_session)):
    
    result = await session.execute(select(MarketModel))
    models = result.scalars().all()
    return models

@router.get("/{market_id}", response_model=MarketResponse)
async def get_markets(market_id: str, session: AsyncSession=Depends(get_session)):
    
    market = await session.get(MarketModel, market_id)
    if market is None:
        raise HTTPException(status_code=404, detail="El mercado no existe")
    return market
    
@router.post("/ingest")
async def ingest_markets(use_case: IngestMarketsUseCase = Depends(get_ingest_use_case)):

    await use_case.execute()

    return {"message":"Ingesta completada"}