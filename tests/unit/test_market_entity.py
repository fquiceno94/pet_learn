from  src.domain.markets.entities import Market

def test_create_market():
    market = Market(
        id="123",
        question="New Rihanna Album before GTA VI?",
        outcome_prices =["Yes", "No"],
        volume = 731560.8738120002,
        liquidity=10751.3089,
        active=True,
        closed=False

        )

    assert market.id == "123"
    assert market.question == "New Rihanna Album before GTA VI?"
    assert market.outcome_prices ==["Yes", "No"]
    assert market.volume ==731560.8738120002
    assert market.liquidity ==10751.3089
    assert market.active ==True
    assert market.closed ==False


    