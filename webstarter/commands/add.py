import typer
from pathlib import Path
from webstarter.core.logger import Logger
from webstarter.utils.file_manager import FileManager

def execute(
    component: str = typer.Argument(..., help="Componente a añadir (ej: navbar, card, footer)")
):
    """
    Añade un componente específico al proyecto actual inyectándolo antes del cierre del body.
    """
    # 1. Detectar el directorio de trabajo actual (donde el usuario quiere añadir el componente)
    cwd = Path.cwd()
    index_path = cwd / "index.html"

    # 2. Verificación de seguridad: ¿Existe el archivo destino?
    if not index_path.exists():
        Logger.error("No se encontró 'index.html'. Asegúrate de estar en la raíz de un proyecto WebStarter.")
        raise typer.Exit(code=1)

    # 3. LOCALIZACIÓN DINÁMICA DE PLANTILLAS:
    # Resolvemos la ruta absoluta del paquete instalado para encontrar la carpeta templates
    base_package_path = Path(__file__).resolve().parent.parent
    template_path = base_package_path / "templates" / "components" / f"{component}.html"

    # 4. Verificación de la plantilla solicitada
    if not template_path.exists():
        Logger.error(f"El componente '{component}' no existe en la biblioteca de WebStarter.")
        raise typer.Exit(code=1)

    try:
        # 5. Lectura del componente y del proyecto actual
        component_html = template_path.read_text(encoding="utf-8")
        current_index = index_path.read_text(encoding="utf-8")

        # 6. Lógica de inyección de código
        if "</body>" in current_index:
            # Insertamos el componente con una indentación limpia antes de cerrar el body
            new_index = current_index.replace("</body>", f"    {component_html}\n</body>")
            FileManager.write_file(index_path, new_index)
            Logger.success(f"Componente '[bold cyan]{component}[/bold cyan]' añadido con éxito a index.html")
        else:
            Logger.error("Error estructural: No se pudo encontrar la etiqueta </body> en index.html")
            raise typer.Exit(code=1)
            
    except Exception as e:
        Logger.error(f"Error inesperado al procesar el archivo: {e}")
        raise typer.Exit(code=1)