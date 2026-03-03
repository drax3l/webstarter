<div align="center">
  <h1>🚀 WebStarter CLI</h1>
  <p><b>La navaja suiza para el scaffolding de proyectos web modernos.</b></p>

  ![Python Version](https://img.shields.io/badge/python-3.10+-blue.svg)
  ![PyPI Version](https://img.shields.io/pypi/v/webstarter-cli.svg)
  ![License](https://img.shields.io/badge/license-MIT-green.svg)
  ![Status](https://img.shields.io/badge/status-stable-brightgreen.svg)
</div>

---

## 📖 Tabla de Contenidos
- [Características](#-características)
- [Instalación](#-instalación)
- [Guía de Uso](#-guía-de-uso)
- [Arquitectura](#-visualización-de-arquitectura)
- [Tecnologías](#-stack-tecnológico)

---

## ✨ Características

| Característica | Descripción |
| :--- | :--- |
| ⚡ **Scaffolding Instantáneo** | Genera estructuras `css/`, `js/` y `assets/` en milisegundos. |
| 🎨 **UI Ready** | Integración nativa con **Bootstrap** y **Modo Oscuro**. |
| 🧩 **Inyección Modular** | Añade componentes como Navbars sin tocar el código manualmente. |
| 🐍 **Python Powered** | Construido con Jinja2, Typer y Rich para máxima estabilidad. |

---

## 📦 Instalación

No necesitas el código fuente. Instala la herramienta globalmente desde **PyPI**:

```bash
pip install webstarter-cli
🚀 Guía de Uso
1. Inicializar Proyecto
Genera una arquitectura profesional lista para producción:

Bash

webstarter create MiWeb --bootstrap --dark
2. Vitaminar con Componentes
Inyecta elementos de UI inteligentes directamente en tu index.html:

Bash

cd MiWeb
webstarter add navbar
🏗️ Visualización de Arquitectura
WebStarter estandariza tu flujo de trabajo con la siguiente jerarquía:

Plaintext

📂 MiProyecto/
├── 📂 assets/img/     # Recursos visuales optimizados
├── 📂 css/            # Estilos base (style.css)
├── 📂 js/             # Scripts de frontend (main.js)
└── 📄 index.html      # Estructura SEO y Bootstrap configurado
🛠️ Stack Tecnológico
Core: Jinja2 (Templating dinámico).

CLI: Typer (Interfaz de comandos rápida).

UI/UX Terminal: Rich (Formateo visual y colores).

Frontend: Bootstrap (Framework de diseño responsivo).

🗺️ Roadmap (Próximamente)
[ ] Soporte para Tailwind CSS.

[ ] Comando webstarter add footer.

[ ] Plantillas para proyectos de React/Vue.

👤 Autor
Desarrollado con dedicación por Alex (drax3l).

"Simplificando la web, un comando a la vez."


## 🗺️ Roadmap de Desarrollo
- [x] Lanzamiento inicial en PyPI (v0.1.0)
- [ ] Implementar comando `webstarter add footer`
- [ ] Añadir validación de nombres de proyecto duplicados
- [ ] Soporte para plantillas de React



---

## 🤝 Contribuciones

¡Las contribuciones son lo que hacen que la comunidad de código abierto sea un lugar increíble para aprender, inspirar y crear! Cualquier contribución que hagas será **muy apreciada**.

1. Haz un **Fork** del proyecto.
2. Crea tu **Feature Branch** (`git checkout -b feature/MejoraIncreible`).
3. Realiza un **Commit** de tus cambios (`git commit -m 'Add: Alguna mejora'`).
4. Haz un **Push** a la rama (`git push origin feature/MejoraIncreible`).
5. Abre un **Pull Request**.

---

## 📄 Licencia

Distribuido bajo la **Licencia MIT**. Consulta el archivo `LICENSE` para obtener más información.

Copyright (c) 2026 Alex (drax3l)