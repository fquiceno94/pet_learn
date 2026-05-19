from src.domain.markets.repositories import MarketRepository
from src.domain.markets.entities import Market

class IngestMarketsUseCase:

    def __init__(self,client, repository):
        self.client = client
        self.repository = repository
    
    async def execute(self):
        
        markets = await self.client.get_markets()
        
        for market_data in markets:
            market = Market(**market_data)
            await self.repository.save(market)