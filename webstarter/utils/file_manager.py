import shutil
from pathlib import Path
from webstarter.core.exceptions import ProjectAlreadyExistsError, WebStarterError
from webstarter.core.logger import Logger

class FileManager:
    """
    Clase encargada de las operaciones físicas de entrada/salida (I/O)
    en el sistema de archivos.
    """

    @staticmethod
    def create_directory(path: Path):
        """Crea un directorio de forma segura."""
        if path.exists():
            # Usamos la excepción personalizada que definiste
            raise ProjectAlreadyExistsError(f"El directorio '{path.name}' ya existe.")
        
        try:
            path.mkdir(parents=True, exist_ok=True)
        except PermissionError:
            raise WebStarterError(f"No tienes permisos para crear la carpeta en: {path}")

    @staticmethod
    def copy_static_files(src: Path, dest: Path):
        """Copia archivos estáticos (CSS, JS, Imágenes) al proyecto."""
        if not src.exists():
            return # Evitamos errores si una carpeta base opcional no existe
        
        try:
            shutil.copytree(src, dest, dirs_exist_ok=True)
        except Exception as e:
            Logger.error(f"Error al copiar archivos estáticos: {e}")

    @staticmethod
    def write_file(path: Path, content: str):
        """Escribe contenido de texto en un archivo con codificación UTF-8."""
        try:
            # Aseguramos que la carpeta que contendrá al archivo exista
            if not path.parent.exists():
                path.parent.mkdir(parents=True, exist_ok=True)
                
            path.write_text(content, encoding="utf-8")
        except Exception as e:
            Logger.error(f"No se pudo escribir el archivo {path.name}: {e}")
            raise WebStarterError(f"Fallo en la escritura de: {path}")