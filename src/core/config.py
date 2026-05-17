from pydantic_settings import BaseSettings

"""
  Este es el archivo más importante de la infraestructura base: centraliza toda la configuración del proyecto (credenciales de DB, variables de entorno,
  etc.). Ningún otro módulo debe leer variables de entorno directamente — todo pasa por aquí.
  
"""

class Settings(BaseSettings):
    DATABASE_URL: str
    ENVIRONMENT: str = "development"
    DEBUG: bool = False

settings = Settings()