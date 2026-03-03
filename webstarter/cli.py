import typer
from webstarter.commands import create, add, init
from webstarter.core.logger import Logger

# Creamos la instancia principal de Typer
app = typer.Typer(
    name="webstarter",
    help="WebStarter: Generador profesional de proyectos web desde la CLI.",
    add_completion=False
)

# Registramos los subcomandos de la carpeta commands
app.command(name="create")(create.execute)
app.command(name="add")(add.execute)
app.command(name="init")(init.execute)

@app.callback(invoke_without_command=True)
def main(ctx: typer.Context):
    """
    Herramienta para automatizar la creación de entornos frontend.
    """
    # Si el usuario no invoca ningún subcomando (ej: solo escribe 'webstarter')
    if ctx.invoked_subcommand is None:
        Logger.welcome() # Mostramos el panel visual pro que creamos en logger.py
        print(ctx.get_help())

if __name__ == "__main__":
    app()