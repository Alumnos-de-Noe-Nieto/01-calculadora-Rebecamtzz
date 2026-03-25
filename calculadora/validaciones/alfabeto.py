"""
Nivel 1: Análisis Léxico - Alfabeto (Σ = {I, V, X, L, C, D, M})
"""

def validar_simbolos(cadena: str) -> bool:
    """
    Valida si todos los caracteres de la cadena pertenecen al alfabeto romano.

    💡 PISTA: Usa .strip() para eliminar espacios en blanco laterales
    💡 PISTA: Retorna False si la cadena está vacía después de eliminar espacios
    💡 PISTA: Recuerda: espacios en blanco laterales NO deben afectar la validación

    Args:
        cadena (str): La cadena a evaluar. Ej: "XIV"

    Returns:
        bool: True si la cadena es completamente válida, False en caso contrario.

    Examples:
        >>> validar_simbolos("XIV")
        True
        >>> validar_simbolos("MCMXCIV")
        True
        >>> validar_simbolos("ABCD")
        False
        >>> validar_simbolos("X-IV")
        False
        >>> validar_simbolos("")
        False
        >>> validar_simbolos("  XIV  ")
        True
    """
        # Primero quitamos los espacios al inicio y al final
    cadena = cadena.strip()

    # Si después de quitar espacios queda vacío, no es válido
    if cadena == "":
        return False

    # Definimos los símbolos romanos permitidos
    simbolos_validos = {"I", "V", "X", "L", "C", "D", "M"}

    # Recorremos la cadena letra por letra
    for caracter in cadena:
        # Si encontramos algo que no es romano, ya no es válido
        if caracter not in simbolos_validos:
            return False

    # Si todo pasó bien, entonces sí es válido
    return True