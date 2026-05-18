# Polymarket Intelligence Engine

Motor de recolección, estructuración y análisis de datos de mercados de predicción.

---

## Metodología de trabajo

Claude Code actúa como mentor técnico. El flujo de cada tarea es:

1. **Explicación** — qué vamos a hacer y por qué
2. **Lectura** — sección específica de documentación antes de escribir código
3. **Tarea concreta** — pequeña y acotada: un archivo, una clase, un test
4. **Intento** — el desarrollador lo implementa
5. **Revisión** — feedback específico sobre qué está mal y por qué
6. **Confirmación** — si está bien, se avanza a la siguiente tarea

### Ciclo TDD obligatorio

```
Red   → escribir el test primero (falla porque el código no existe)
Green → escribir el código mínimo para que el test pase
Refactor → limpiar sin romper los tests
```

### Cómo pedir trabajo

```
# Empezar algo nuevo
Vamos a trabajar [qué]. Estoy en Fase [N].

# Cuando algo no funciona
Estoy en [fase/tarea].
Hice esto: [código o descripción]
El error es: [error exacto]
Ya intenté: [qué probé]

# Revisión de código
Revisa esto con criterio de producción.
No solo estilo — qué va a fallar en casos borde o a escala.
```

---

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


