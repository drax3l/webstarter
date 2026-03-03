import os

def crear_estructura(nombre_proyecto):
    # Crear carpeta principal
    os.makedirs(nombre_proyecto, exist_ok=True)

    # Crear subcarpetas
    os.makedirs(f"{nombre_proyecto}/css", exist_ok=True)
    os.makedirs(f"{nombre_proyecto}/js", exist_ok=True)
    os.makedirs(f"{nombre_proyecto}/assets/img", exist_ok=True)

    print("✅ Carpetas creadas correctamente")


def crear_html(nombre_proyecto):
    contenido_html = """<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Mi Página Web</title>
    <link rel="stylesheet" href="css/style.css">
</head>
<body>

    <header>
        <h1>Bienvenido a mi proyecto</h1>
    </header>

    <main>
        <p>Proyecto generado automáticamente con Python 🚀</p>
        <button onclick="saludar()">Haz clic</button>
    </main>

    <script src="js/script.js"></script>
</body>
</html>
"""

    with open(f"{nombre_proyecto}/index.html", "w", encoding="utf-8") as f:
        f.write(contenido_html)

    print("✅ index.html creado")


def crear_css(nombre_proyecto):
    contenido_css = """body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
    background-color: #f4f4f4;
    text-align: center;
}

header {
    background: #333;
    color: white;
    padding: 20px;
}

button {
    padding: 10px 20px;
    cursor: pointer;
}
"""

    with open(f"{nombre_proyecto}/css/style.css", "w", encoding="utf-8") as f:
        f.write(contenido_css)

    print("✅ style.css creado")


def crear_js(nombre_proyecto):
    contenido_js = """function saludar() {
    alert("¡Hola! Proyecto creado automáticamente 🎉");
}
"""

    with open(f"{nombre_proyecto}/js/script.js", "w", encoding="utf-8") as f:
        f.write(contenido_js)

    print("✅ script.js creado")


def main():
    nombre = input("Ingrese el nombre del proyecto: ")
    
    crear_estructura(nombre)
    crear_html(nombre)
    crear_css(nombre)
    crear_js(nombre)

    print(f"\n🚀 Proyecto '{nombre}' creado exitosamente")


if __name__ == "__main__":
    main()