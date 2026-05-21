import pandera.pandas as pa

class MarketSchema(pa.DataFrameModel):
    id: pa.typing.Series[str]
    question: pa.typing.Series[str]
    outcomePrices: pa.typing.Series[str]
    volume: pa.typing.Series[str]
    liquidity: pa.typing.Series[str]
    active: pa.typing.Series[bool]
    closed: pa.typing.Series[bool]