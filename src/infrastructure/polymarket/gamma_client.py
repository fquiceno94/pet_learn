import httpx

class GammaClient():
    BASE_URL = "https://gamma-api.polymarket.com"

    def __init__(self):
        self.client = httpx.AsyncClient(base_url=self.BASE_URL)

    async def get_markets(self) -> list[dict]:
        
        response = await self.client.get("/markets")
        response.raise_for_status()

        return response.json()