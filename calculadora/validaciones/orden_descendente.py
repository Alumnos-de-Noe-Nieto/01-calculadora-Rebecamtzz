"""
Nivel 4: Validación de orden descendente.

Los símbolos deben ir en orden descendente de valor (izquierda a derecha).
Excepción: las 6 formas sustractivas válidas.
Ejemplos válidos: XVI, MDCLXVI, XIV (sustracción válida)
Ejemplos inválidos: IVX, IIV, VIV
"""

def validar_orden_descendente(cadena: str) -> bool:

    #valores de los símbolos
    valores= {
        "I": 1, "V": 5, "X": 10,
        "L": 50, "C": 100, "D": 500, "M": 1000
    }

    # sustracciones válidas
    sustracciones_validas = {"IV", "IX", "XL", "XC", "CD", "CM"}

    i = 0

    # recorre con índice
    while i < len(cadena) - 1:

        # detecta sustracción válida
        if cadena[i:i+2] in sustracciones_validas:

            # evita repetición
            if i > 0 and cadena[i-1] == cadena[i]:
                return False

            # verificar que después siga el orden descendente
            if i + 2 < len(cadena) and  valores[cadena[i+1]] < valores[cadena[i+2]]:
                    return False

            i += 2  # avanza

        else:
            # verifica orden descendente normal
            if valores[cadena[i]] < valores[cadena[i+1]]:
                return False

            i += 1

    return True
