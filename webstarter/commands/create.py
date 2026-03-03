import typer
from typing import Optional
from webstarter.core.generator import ProjectGenerator
from webstarter.core.logger import Logger
from webstarter.core.exceptions import WebStarterError
from webstarter.core.validator import Validator # Importación necesaria

def execute(
    name: str = typer.Argument(..., help="Nombre de la carpeta del proyecto"),
    bootstrap: bool = typer.Option(False, "--bootstrap", "-b", help="Incluye soporte para Bootstrap"),
    dark: bool = typer.Option(False, "--dark", "-d", help="Configura el proyecto en modo oscuro")
):
    """
    Crea un nuevo proyecto web con una estructura profesional.
    """
    try:
        # VALIDACIÓN PREVENTIVA: Aseguramos que el nombre sea apto
        Validator.validate_name(name)
        
        # Instanciamos el generador con las opciones elegidas
        generator = ProjectGenerator(
            project_name=name,
            bootstrap=bootstrap,
            dark_mode=dark
        )
        
        # Feedback visual para el usuario
        Logger.info(f"Construyendo proyecto: [bold cyan]{name}[/bold cyan]...")
        
        # Ejecución del motor de generación
        generator.build()
        
    except WebStarterError as e:
        # Errores controlados de nuestra aplicación
        Logger.error(str(e))
        raise typer.Exit(code=1)
    except Exception as e:
        # Errores inesperados del sistema
        Logger.error(f"Ocurrió un error inesperado: {e}")
        raise typer.Exit(code=1)