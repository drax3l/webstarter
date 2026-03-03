from pathlib import Path

class ProjectStructure:

    def __init__(self, name: str):
        self.project_path = Path(name)

    def create_folders(self):
        folders = [
            self.project_path,
            self.project_path / "css",
            self.project_path / "js",
            self.project_path / "assets" / "img"
        ]

        for folder in folders:
            folder.mkdir(parents=True, exist_ok=True)

        print("✅ Estructura creada correctamente")