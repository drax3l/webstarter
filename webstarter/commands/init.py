import typer
from pathlib import Path
from webstarter.core.logger import Logger

def execute():
    """
    Inicializa una configuración de WebStarter en el directorio actual.
    """
    Logger.info("Inicializando configuración de WebStarter...")
    
    # 1. Definimos la ruta del archivo de configuración en el directorio actual
    config_path = Path.cwd() / ".webstarter.json"
    
    # 2. Verificamos si ya existe para evitar sobrescribir datos del usuario
    if not config_path.exists():
        try:
            # 3. Creamos un archivo de configuración base
            # Esto permitirá que en el futuro tu CLI sepa qué versión se usó o qué plugins hay
            config_content = '{"version": "0.1.0", "plugins": [], "created_at": "2026"}'
            config_path.write_text(config_content, encoding="utf-8")
            
            Logger.success("Archivo de configuración '.webstarter.json' creado exitosamente.")
            Logger.success("Entorno preparado.")
        except Exception as e:
            Logger.error(f"No se pudo crear el archivo de configuración: {e}")
            raise typer.Exit(code=1)
    else:
        Logger.warning("El entorno ya contiene una configuración de WebStarter activa.")