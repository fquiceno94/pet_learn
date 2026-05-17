# pet_learn
Petproject to learn many technologies



# Antes de pasar a la fase 1:
-   uv venv .venv && source .venv/bin/activate       
-   Luego agrega las dependencias de la Fase 0 al pyproject.toml: uv add pydantic pydantic-settings  
-  Revisar que el config.py lea las variables de entorno corrctamente: python -c "from src.core.config import settings; print(settings.DATABASE_URL)"