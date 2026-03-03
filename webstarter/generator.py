from pathlib import Path
from .structure import ProjectStructure
from .templates import Templates


class ProjectGenerator:

    def __init__(self, name: str, title: str):
        self.name = name
        self.title = title
        self.structure = ProjectStructure(name)

    def generate(self):
        self.structure.create_folders()

        base_path = Path(self.name)

        # Crear archivos
        (base_path / "index.html").write_text(
            Templates.html(self.title), encoding="utf-8"
        )

        (base_path / "css" / "style.css").write_text(
            Templates.css(), encoding="utf-8"
        )

        (base_path / "js" / "script.js").write_text(
            Templates.js(), encoding="utf-8"
        )

        print(f"🚀 Proyecto '{self.name}' generado con éxito")