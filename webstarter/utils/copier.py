import shutil
from pathlib import Path
from webstarter.core.logger import Logger

class Copier:
    """
    Clase utilitaria encargada de la transferencia física de directorios
    y archivos de plantillas hacia el proyecto de destino.
    """

    @staticmethod
    def copy_template_folder(src: Path, dest: Path):
        """
        Copia recursivamente una carpeta completa al destino especificado.
        
        Args:
            src (Path): Carpeta de origen (dentro de templates).
            dest (Path): Carpeta de destino (dentro del nuevo proyecto).
        """
        if not src.exists():
            Logger.warning(f"La fuente de plantillas '{src.name}' no existe. Saltando copia.")
            return

        try:
            # dirs_exist_ok=True permite fusionar carpetas si ya existen
            shutil.copytree(src, dest, dirs_exist_ok=True)
        except Exception as e:
            Logger.error(f"Error crítico al copiar archivos de {src.name}: {e}")
            raise