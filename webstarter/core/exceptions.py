class WebStarterError(Exception):
    """Error base para la aplicación."""
    pass

class ProjectAlreadyExistsError(WebStarterError):
    """Se lanza si la carpeta de destino ya existe."""
    pass

class TemplateNotFoundError(WebStarterError):
    """Se lanza si no se encuentra una carpeta de plantilla."""
    pass

# --- ADICIONES RECOMENDADAS PARA COMPLETAR EL CORE ---

class ValidationError(WebStarterError):
    """Se lanza si el nombre del proyecto o componente es inválido."""
    pass

class InjectionError(WebStarterError):
    """Se lanza si falla la inyección de componentes (ej. falta etiqueta </body>)."""
    pass