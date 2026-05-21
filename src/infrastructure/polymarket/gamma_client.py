import json
import httpx
import pandas as pd
from src.infrastructure.polymarket.schemas import MarketSchema

class GammaClient():
    BASE_URL = "https://gamma-api.polymarket.com"

    def __init__(self):
        self.client = httpx.AsyncClient(base_url=self.BASE_URL)

    async def get_markets(self) -> list[dict]:
        
        try:
            response = await self.client.get("/markets")
            response.raise_for_status()
        except httpx.HTTPStatusError as e:
            raise RuntimeError(f"Gamma API error: {e.response.status_code}") from e
        except httpx.RequestError as e:
            raise RuntimeError(f"No se pudo conectar a Gamma API: {e}") from e
        
        data = response.json()
        df = pd.DataFrame(data)
        MarketSchema.validate(df)

        return [
            {
                "id": m["id"],
                "question": m["question"],
                "outcome_prices": json.loads(m["outcomePrices"]),
                "volume": float(m["volume"]),
                "liquidity": float(m["liquidity"]),
                "active": m["active"],
                "closed": m["closed"],
            }
            for m in data
        ]