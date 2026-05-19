import respx
import httpx
import pytest

from src.infrastructure.polymarket.gamma_client import GammaClient

@respx.mock
async def test_get_markets_returns_list():
    # 1. configurar el mock  
    respx.get("https://gamma-api.polymarket.com/markets").mock(
        return_value=httpx.Response(200, json=[{"id": "1", "question": "Test?"}])   
    )

    # 2. llamar al cliente   
    client = GammaClient()
    result = await client.get_markets()

    # 3. verificar     
    assert len(result) == 1
    assert result[0]["id"] == "1"

@respx.mock
async def test_get_markets_raises_on_server_error():
    respx.get("https://gamma-api.polymarket.com/markets").mock(
        return_value=httpx.Response(500, json=[{"id": "1", "question": "Test?"}])   
    )

    with pytest.raises(httpx.HTTPStatusError):
        client = GammaClient()
        await client.get_markets()
