import argparse
from .generator import ProjectGenerator


def run():
    parser = argparse.ArgumentParser(
        description="WebStarter - Generador profesional de proyectos web"
    )

    parser.add_argument("name", help="Nombre del proyecto")
    parser.add_argument("--title", default="Mi Página Web",
                        help="Título de la página")

    args = parser.parse_args()

    generator = ProjectGenerator(args.name, args.title)
    generator.generate()