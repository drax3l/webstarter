from pathlib import Path
from jinja2 import Environment, FileSystemLoader
from webstarter.core.logger import Logger
from webstarter.utils.file_manager import FileManager
from webstarter.core.project_builder import ProjectBuilder
from webstarter.utils.copier import Copier # Importación añadida

class ProjectGenerator:
    def __init__(self, project_name: str, bootstrap: bool = False, dark_mode: bool = False, multi_page: bool = False):
        self.project_name = project_name
        self.bootstrap = bootstrap
        self.dark_mode = dark_mode
        self.multi_page = multi_page # Nueva opción para proyectos MPA
        self.target_path = Path.cwd() / project_name
        
        # Resolución de ruta absoluta para las plantillas instaladas
        self.template_dir = Path(__file__).resolve().parent.parent / "templates"
        
        # Configuración de Jinja2
        self.env = Environment(loader=FileSystemLoader(str(self.template_dir)))

    def build(self):
        """Ejecuta el flujo completo de construcción del proyecto."""
        try:
            # 1. Crear estructura física de carpetas
            ProjectBuilder.init_structure(self.target_path)
            
            # 2. Generar index.html principal
            self._generate_index()
            
            # 3. Copiar assets estáticos base (CSS/JS)
            base_templates = self.template_dir / "base"
            FileManager.copy_static_files(base_templates / "css", self.target_path / "css")
            FileManager.copy_static_files(base_templates / "js", self.target_path / "js")
            
            # 4. Lógica Multi-Página (Si se solicita)
            if self.multi_page:
                self._generate_multipage()
            
            Logger.success(f"Proyecto '[bold cyan]{self.project_name}[/bold cyan]' generado correctamente.")
            
        except Exception as e:
            Logger.error(f"Fallo en la construcción del proyecto: {e}")
            raise

    def _generate_index(self):
        """Renderiza la plantilla index.html aplicando las opciones elegidas."""
        template = self.env.get_template("base/index.html")
        output = template.render(
            title=self.project_name,
            use_bootstrap=self.bootstrap,
            dark_mode=self.dark_mode
        )
        FileManager.write_file(self.target_path / "index.html", output)

    def _generate_multipage(self):
        """Genera archivos adicionales para una arquitectura de varias páginas."""
        Logger.info("Añadiendo soporte multi-página...")
        
        # Renderizar página About (Nosotros)
        template_about = self.env.get_template("multipage/about.html")
        output_about = template_about.render(
            title=self.project_name,
            use_bootstrap=self.bootstrap,
            dark_mode=self.dark_mode
        )
        FileManager.write_file(self.target_path / "about.html", output_about)
        
        # Copiar lógica de navegación usando Copier
        # Esto copia el contenido de multipage/js a la carpeta js del proyecto
        multi_js_src = self.template_dir / "multipage"
        if (multi_js_src / "router.js").exists():
            router_content = (multi_js_src / "router.js").read_text(encoding="utf-8")
            FileManager.write_file(self.target_path / "js" / "router.js", router_content)