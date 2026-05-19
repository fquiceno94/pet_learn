import pytest 
from testcontainers.postgres import PostgresContainer
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

from src.infrastructure.database.models import Base
from src.domain.markets.entities import Market
from src.infrastructure.database.models import MarketModel
from src.infrastructure.database.repositories import PostgresMarketRepository

"""
  Lo que hace cada bloque de la fixture:      
                                          
  - PostgresContainer("postgres:16") — levanta un contenedor PostgreSQL real
  - get_connection_url().replace(...) — convierte la URL de psycopg2 a asyncpg (el driver async que usamos)                        
  - create_async_engine(url) — crea el motor de conexión
  - Base.metadata.create_all — crea las tablas en esa DB temporal                                                                  
  - sessionmaker(...) — fábrica de sesiones                                                                                      
  - yield session — entrega la sesión al test, espera que termine, luego limpia                                                    
  - engine.dispose() — cierra las conexiones al final                
"""

@pytest.fixture
async def db_session():

    with PostgresContainer("postgres:16") as postgres:

        url = postgres.get_connection_url().replace(
              "postgresql+psycopg2", "postgresql+asyncpg"
          )
        
        engine = create_async_engine(url)

        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)

        async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

        async with async_session() as session:
            yield session
        
        await engine.dispose()


async def test_save_market(db_session):
    market = Market(
        id="1",                                                                                                                  
        question="Will it happen?",
        outcome_prices=["Yes", "No"],                                                                                            
        volume=100.0,                   
        liquidity=50.0,                                                                                                          
        active=True,                                                                                                             
        closed=False
    )

    repo = PostgresMarketRepository(db_session)
    await repo.save(market)

    result = await db_session.get(MarketModel, "1")
    assert result is not None
    assert result.id == "1"
