class Templates:

    @staticmethod
    def html(title: str):
        return f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <link rel="stylesheet" href="css/style.css">
</head>
<body>

    <header>
        <h1>{title}</h1>
    </header>

    <main>
        <p>Proyecto generado automáticamente con Python 🚀</p>
        <button onclick="saludar()">Haz clic</button>
    </main>

    <script src="js/script.js"></script>
</body>
</html>
"""

    @staticmethod
    def css():
        return """body {
    font-family: Arial, sans-serif;
    background-color: #f4f4f4;
    text-align: center;
}
"""

    @staticmethod
    def js():
        return """function saludar() {
    alert("Proyecto generado correctamente 🚀");
}
"""