import re
from webstarter.core.exceptions import WebStarterError # Usamos nuestra excepción base

class Validator:
    """
    Clase encargada de validar las entradas del usuario para asegurar
    la integridad del sistema de archivos.
    """

    @staticmethod
    def validate_name(name: str) -> bool:
        """
        Valida que el nombre del proyecto sea seguro.
        
        Reglas:
        - Solo letras (A-Z, a-z), números (0-9).
        - Permite guiones (-) y guiones bajos (_).
        - No permite espacios ni caracteres especiales.
        """
        
        # Expresión regular: permite letras, números, guiones y guiones bajos
        pattern = r'^[a-zA-Z0-9_-]+$'
        
        if not re.match(pattern, name):
            raise WebStarterError(
                f"El nombre '{name}' es inválido. "
                "Usa solo letras, números, guiones (-) o guiones bajos (_), sin espacios."
            )
            
        # Opcional: Evitar nombres demasiado cortos
        if len(name) < 2:
            raise WebStarterError("El nombre del proyecto es demasiado corto.")

        return True