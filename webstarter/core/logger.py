from rich.console import Console
from rich.panel import Panel

# Inicializamos la consola globalmente para este módulo
console = Console()

class Logger:
    @staticmethod
    def welcome():
        """Muestra un panel de bienvenida al iniciar la herramienta."""
        console.print(
            Panel.fit(
                "🚀 [bold cyan]WebStarter CLI[/bold cyan]\n[italic white]Tu generador profesional de proyectos web[/italic white]",
                border_style="blue",
                title="v0.1.0"
            )
        )

    @staticmethod
    def info(message: str):
        """Muestra un mensaje informativo en azul."""
        console.print(f"[bold blue]INFO:[/bold blue] {message}")

    @staticmethod
    def success(message: str):
        """Muestra un mensaje de éxito en verde."""
        console.print(f"[bold green]SUCCESS:[/bold green] {message}")

    @staticmethod
    def error(message: str):
        """Muestra un mensaje de error crítico en rojo."""
        console.print(f"[bold red]ERROR:[/bold red] {message}")

    @staticmethod
    def warning(message: str):
        """Muestra un aviso o advertencia en amarillo."""
        console.print(f"[bold yellow]WARNING:[/bold yellow] {message}")