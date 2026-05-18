# pet_learn
Petproject to learn many technologies

# APIS usadas
- https://gamma-api.polymarket.com/markets?limit=1  


# Antes de pasar a la fase 1:
-   uv venv .venv && source .venv/bin/activate       
-   Luego agrega las dependencias de la Fase 0 al pyproject.toml: uv add pydantic pydantic-settings
    *   uv add instala una dependencia y la registra en pyproject.toml.
    *   --dev le dice a uv que estas son dependencias de desarrollo (Sin --dev, la dependencia queda en [project.dependencies])
    *   
-  Revisar que el config.py lea las variables de entorno corrctamente: python -c "from src.core.config import settings; print(settings.DATABASE_URL)"


# Documentacion puntual leia para el proyecto:
- https://docs.astral.sh/uv/concepts/projects/init/
- https://docs.pydantic.dev/latest/concepts/pydantic_settings/
- https://docs.docker.com/compose/intro/compose-application-model/
- https://hub.docker.com/_/postgres
- https://docs.pydantic.dev/latest/concepts/pydantic_settings/#dotenv-env-support
- https://pydantic.dev/docs/validation/latest/concepts/pydantic_settings/#dotenv-env-support


