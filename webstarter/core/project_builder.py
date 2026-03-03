from pathlib import Path
from webstarter.utils.file_manager import FileManager

class ProjectBuilder:
    """
    Clase responsable de construir la estructura física de directorios
    del nuevo proyecto web.
    """

    @staticmethod
    def init_structure(base_path: Path):
        """
        Crea el esqueleto de carpetas inicial del proyecto.
        
        Args:
            base_path (Path): La ruta raíz donde se creará el proyecto.
        """
        # 1. Crear el directorio raíz del proyecto
        FileManager.create_directory(base_path)

        # 2. Definir la lista de subcarpetas necesarias para un proyecto profesional
        folders = [
            "css",          # Para hojas de estilo
            "js",           # Para lógica de scripts
            "assets/img",   # Para recursos multimedia e imágenes
        ]

        # 3. Crear cada subcarpeta de forma iterativa
        for folder in folders:
            subfolder_path = base_path / folder
            FileManager.create_directory(subfolder_path)