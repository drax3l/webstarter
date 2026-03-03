import pytest
from webstarter.core.validator import Validator

def test_name_validation():
    # El validador debe aceptar nombres simples
    assert Validator.validate_name("mi-proyecto") == True
    # El validador debe fallar con espacios
    with pytest.raises(Exception):
        Validator.validate_name("proyecto con espacios")