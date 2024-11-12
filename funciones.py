from validaciones import *
import random
import os
NUMERO_DE_LISTA = 0
VOTOS_TURNO_MAÑANA = 1
VOTOS_TURNO_TARDE = 2
VOTOS_TURNO_NOCHE = 3
PORCENTAJE_VOTOS = 4


def limpiar_pantalla():
    """borra informacion antigua en la consola para presentar nueva
    """
    import os
    os.system("cls")


def pausar():
    """_el programa es pausado hasta presionar una tecla
    """
    import os
    os.system("pause")


def menu() -> str:
    """muestra un menu de opciones a elegir

    Returns:
        str: devuelve la opcion elegida
    """

    limpiar_pantalla()
    print(f"{'Menu de Opciones':^50s}")

    print("1- cargar votos")
    print("2- mostrar votos")
    print("3- ordenar votos por turno mañana")
    print("4- no te voto nadie")
    print("5- turno que mas fue a votar")
    print("6- Habra ballotage?")
    print("7- realizar segunda vuelta")
    print("8- Desea salir")

    return input("Ingrese una opcion: ")


def inicializar_matriz(cantidad_filas: int, cantidad_columnas: int, valor_inicial: any) -> list:
    """Crea una matriz con lista anidadas con los elementos inicializados en el valor inicial

    Args:
        cantidad_filas (int): cantidas de listas que tendra la matriz
        cantidad_columnas (_type_): cantidad de elementos que posee cada lista interna
        valor_inicial (any): valor deseados con que se quiere cada uno de los elementos
    Returns:
        list: retorna una matriz 
    """
    matriz = []
    for i in range(cantidad_filas):
        fila = [valor_inicial] * cantidad_columnas
        matriz += [fila]
    return matriz


def cargar_matriz_secuencial(matriz: list):
    """carga de elementos de una triz desde el primero hasta el ultimo en forma sucesiva"""
    for i in range(len(matriz)):
        numero_lista = cargar_numero(
            "Ingrese el numero de lista de 3 cifras: ", "Error, ingrese nuevamente: ", 100, 999)
        cantidad_votos_mañana = cargar_numero(
            "Ingrese la cantidad de votos del turno diurno: ", "Error, ingrese nuevamente", 0, 1000000000)
        cantidad_votos_tarde = cargar_numero(
            "Ingrese la cantidad de votos del turno de la tarde: ", "Error, ingrese nuevamente", 0, 1000000000)
        cantidad_votos_noche = cargar_numero(
            "Ingrese la cantidad de votos del turno de la noche: ", "Error, ingrese nuevamente", 0, 1000000000)

        matriz[i][NUMERO_DE_LISTA] = numero_lista
        matriz[i][VOTOS_TURNO_MAÑANA] = cantidad_votos_mañana
        matriz[i][VOTOS_TURNO_TARDE] = cantidad_votos_tarde
        matriz[i][VOTOS_TURNO_NOCHE] = cantidad_votos_noche
    cargar_matriz_porcentajes(matriz)


def cargar_numero(mensaje: str, mensaje_error, min: int, max: int):
    """Permite el ingreso de un numero entero positivo segun los limites establecidos 

    Args:
        mensaje (str): mensaje pautado para el ingreso numerico
        mensaje_error (_type_): mensaje si llegase a fallar el ingreso
        min (int): limite inferior del rango deseado
        max (int): limite superior del rango deseado
    Returns:
        _type_: _description_
    """
    while True:
        numero = input(mensaje)
        if numero.isdigit():
            numero = int(numero)
            if validar_numero(numero, min, max):
                return numero
            else:
                print(mensaje_error)
        else:
            print(mensaje_error)


def calcular_voto_total_de_votacion(matriz) -> list:
    """totaliza los votos de todas las listas
    return: la cantidad de votos total de la eleccion
    """
    acumulador = 0
    for i in range(len(matriz)):
        acumulador += (matriz[i][VOTOS_TURNO_MAÑANA] + matriz[i]
                       [VOTOS_TURNO_TARDE]+matriz[i][VOTOS_TURNO_NOCHE])
    return acumulador


def calcular_porcentaje_de_votos(cantidad_votos_lista: int, cantidad_votos_totales_eleccion):
    """determina el porcentaje de votos que saco la lista en relacion a la demas

    Args:
        cantidad_votos_lista (int): _por lista
        cantidad_votos_totales_eleccion (_type_):cantidad de votos realizados por todos los alumnos

    Returns:
        _type_: _description_
    """
    return (cantidad_votos_lista / cantidad_votos_totales_eleccion)*100


def cargar_matriz_porcentajes(matriz):
    """carga con un string el porcentaje de votos obtenidos sobre el final de las votaciones por cada lista

    Args:
        matriz (list_): _matriz a cargar
    """
    votos_totales = calcular_voto_total_de_votacion(matriz)
    for i in range(len(matriz)):
        cantidad_votos_lista = (
            matriz[i][VOTOS_TURNO_MAÑANA] + matriz[i][VOTOS_TURNO_TARDE]+matriz[i][VOTOS_TURNO_NOCHE])
        matriz[i][PORCENTAJE_VOTOS] = calcular_porcentaje_de_votos(
            cantidad_votos_lista, votos_totales)


def mostrar_matriz(matriz):
    for i in range(len(matriz)):
        print("-------------------------------------------------------------------")
        print(f"Lista: {matriz[i][NUMERO_DE_LISTA]}")
        print(f"Cantidad de Votos Turno Mañana: {
              matriz[i][VOTOS_TURNO_MAÑANA]}")
        print(f"Cantidad de Votos Turno Tarde: {matriz[i][VOTOS_TURNO_TARDE]}")
        print(f"Cantidad de Votos Turno Noche: {matriz[i][VOTOS_TURNO_NOCHE]}")
        print(f"Porcentaje de los Votos: {matriz[i][PORCENTAJE_VOTOS]:.2f}%")


def ordernar_matriz(matriz: list, campo_de_orden: int, criterio: str = "descendente"):
    for i in range(len(matriz)-1):
        for j in range(i+1, len(matriz)):
            if (criterio == "descendente" and matriz[i][campo_de_orden] < matriz[j][campo_de_orden]) or (criterio == "ascendente" and matriz[i][campo_de_orden] > matriz[j][campo_de_orden]):
                auxiliar = matriz[i]
                matriz[i] = matriz[j]
                matriz[j] = auxiliar


def buscar_porcentaje_menos_votado(matriz: list, target: int):
    bandera_menos_votado = False
    for i in range(len(matriz)):
        if matriz[i][PORCENTAJE_VOTOS] < target:
            print(f"la lista {matriz[i][NUMERO_DE_LISTA]} tiene {
                  matriz[i][PORCENTAJE_VOTOS]:.2f}% siendo de los menos votado")
            bandera_menos_votado = True
    if bandera_menos_votado == False:
        print(f"Ninguna lista tuvo menos del {target:.2f} %")


def buscar_turno_con_mayor_votos(matriz):
    punto_maximo = 0
    total_votos_turno_mañana = 0
    total_votos_turno_tarde = 0
    total_votos_turno_noche = 0

    for i in range(len(matriz)):
        total_votos_turno_mañana += matriz[i][VOTOS_TURNO_MAÑANA]
        total_votos_turno_tarde += matriz[i][VOTOS_TURNO_TARDE]
        total_votos_turno_noche += matriz[i][VOTOS_TURNO_NOCHE]

    if total_votos_turno_mañana >= total_votos_turno_tarde and total_votos_turno_mañana >= total_votos_turno_noche:
        print(" la mañana fue el turno donde mas se voto")
    elif total_votos_turno_tarde >= total_votos_turno_noche:
        print(" la  tarde fue el turno donde mas se voto")
    else:
        print("la noche fue donde mas se voto")


def determinar_realizacion_ballotage(matriz: list, target: int):
    bandera_ballotage = True
    for i in range(len(matriz)):
        if matriz[i][PORCENTAJE_VOTOS] > target:
            print(f"la lista {matriz[i][NUMERO_DE_LISTA]} tiene {
                  matriz[i][PORCENTAJE_VOTOS]:.2f}%  por lo que no se realizara el ballotage")
            bandera_ballotage = False

    if bandera_ballotage == True:
        print("ninguna lista saco mas de 50% por ello se va a ballotage")

    return bandera_ballotage


def cargar_matriz_secuencial_ballotage(matriz: list):
    """carga de elementos de una matriz desde el primero hasta el ultimo en forma sucesiva"""

    cantidad_alumnos_diurno = cargar_numero(
        "Ingrese la cantidad de alumnos que votaron en la mañana:  ", "Error, ingrese nuevamente: ", 0,  100000000)
    cantidad_alumnos_tarde = cargar_numero(
        "Ingrese la cantidad de alumnos que votaron en la tarde: ", "Error, ingrese nuevamente: ", 0,  100000000)

    cantidad_alumnos_noche = cargar_numero(
        "Ingrese la cantidad de alumnos que votaron en la noche: ", "Error, ingrese nuevamente: ", 0,  100000000)

    matriz[0][VOTOS_TURNO_MAÑANA] = random.randint(0, cantidad_alumnos_diurno)
    matriz[0][VOTOS_TURNO_TARDE] = random.randint(0, cantidad_alumnos_tarde)
    matriz[0][VOTOS_TURNO_NOCHE] = random.randint(0, cantidad_alumnos_noche)

    matriz[1][VOTOS_TURNO_MAÑANA] = cantidad_alumnos_diurno - \
        matriz[0][VOTOS_TURNO_MAÑANA]
    matriz[1][VOTOS_TURNO_TARDE] = cantidad_alumnos_tarde - \
        matriz[0][VOTOS_TURNO_TARDE]
    matriz[1][VOTOS_TURNO_NOCHE] = cantidad_alumnos_noche - \
        matriz[0][VOTOS_TURNO_NOCHE]
    cargar_matriz_porcentajes(matriz)
