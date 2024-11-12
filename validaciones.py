NUMERO_DE_LISTA = 0
VOTOS_TURNO_MAÑANA =1
VOTOS_TURNO_TARDE = 2
VOTOS_TURNO_NOCHE = 3
PORCENTAJE_VOTOS = 4

def validar_numero(numero: int, limite_inferior: int, limite_superior: int) -> bool:
    """Verifica que el numero este dentro de los limites 

    Args:
        numero (int): numero a verificar
        limite_inferior (int): _rango inferior 
        limite_superior (int): limite superior del rango por defecto es infinito

    Returns:
        bool: devuelve True si es un entero positivo false caso contrario
    """

    if numero >= limite_inferior and numero <= limite_superior:
        return True
    else:
        print(" el numero no esta dentro del rango")
        return False

NUMERO_DE_LISTA = 0
VOTOS_TURNO_MAÑANA =1
VOTOS_TURNO_TARDE = 2
VOTOS_TURNO_NOCHE = 3
PORCENTAJE_VOTOS = 4

def validar_numero(numero: int, limite_inferior: int, limite_superior: int) -> bool:
    """Verifica que el numero este dentro de los limites 

    Args:
        numero (int): numero a verificar
        limite_inferior (int): _rango inferior 
        limite_superior (int): limite superior del rango por defecto es infinito

    Returns:
        bool: devuelve True si es un entero positivo false caso contrario
    """

    if numero >= limite_inferior and numero <= limite_superior:
        return True
    else:
        print(" el numero no esta dentro del rango")
        return False
