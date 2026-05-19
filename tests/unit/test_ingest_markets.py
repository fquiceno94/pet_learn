import pytest
from src.application.markets.ingest_markets import IngestMarketsUseCase

class FakeGammaClient:
    async def get_markets(self)-> list[dict]:
        return [{"id": "1", "question": "Test?", "outcome_prices": ["Yes", "No"], "volume": 100.0, "liquidity": 50.0, "active": True, "closed": False}]  
    
class FakeMarketRepository:
    def __init__(self):
        self.saved = []

    async def save(self, market):
        self.saved.append(market)

async def test_ingest_markets_saves_market():

    gamma_client = FakeGammaClient()
    repository_market = FakeMarketRepository()
    
    ingest = IngestMarketsUseCase(client=gamma_client, repository=repository_market)

    await ingest.execute()

    assert len(repository_market.saved) == 1
    assert repository_market.saved[0].id == "1"