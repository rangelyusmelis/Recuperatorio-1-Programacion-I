from funciones import *
import random

NUMERO_DE_LISTA = 0
VOTOS_TURNO_MAÑANA = 1
VOTOS_TURNO_TARDE = 2
VOTOS_TURNO_NOCHE = 3
PORCENTAJE_VOTOS = 4

matriz_votos = inicializar_matriz(5, 5, 0)

flag_1 = False
flag_ballotage_2 = False
seguir = 's'

while seguir == "s":

    match menu():
        case "1":
            cargar_matriz_secuencial(matriz_votos)
            flag_1 = True
            print("la carga fue realizada")

        case "2":

            if flag_1 == False:
                print("Para poder ver la matriz deberas cargarla antes")

            else:
                mostrar_matriz(matriz_votos)

        case "3":
            if (flag_1 == False):
                print("Para poder ordenar la matriz deberas cargarla antes")

            else:
                print(
                    "\n matriz ordenada por tuno mañana :\n")
                ordernar_matriz(
                    matriz_votos, VOTOS_TURNO_MAÑANA, "descendente")
                mostrar_matriz(matriz_votos)

        case "4":
            if (flag_1 == False):
                print("Para poder ver quien tuvo menos del 5 deberas cargar antes")
            else:
                buscar_porcentaje_menos_votado(matriz_votos, 5)

        case "5":
            if (flag_1 == False):
                print("Para poder ver el turno mas votado deberas cargar antes")
            else:
                buscar_turno_con_mayor_votos(matriz_votos)

        case "6":
            if (flag_1 == False):
                print("Para poder ver si hay ballotage deberas cargar antes")
            else:
                ballotage = determinar_realizacion_ballotage(matriz_votos, 50)
                flag_ballotage_2 = True

        case "7":
            if (flag_ballotage_2 == False):
                print(
                    "primero deberas eejecutar el paso 6 de la determinacion del ballotage")
            else:

                if ballotage == True:
                    ordernar_matriz(
                        matriz_votos, PORCENTAJE_VOTOS, "descendente")
                    print(f"los candidatos mas votados son la lista numero {
                        matriz_votos[0][NUMERO_DE_LISTA]} y la lista numero {matriz_votos[1][NUMERO_DE_LISTA]} ")

                    matriz_ballotage = inicializar_matriz(2, 5, 0)
                    matriz_ballotage[0][NUMERO_DE_LISTA] = matriz_votos[0][NUMERO_DE_LISTA]
                    matriz_ballotage[1][NUMERO_DE_LISTA] = matriz_votos[1][NUMERO_DE_LISTA]

                    cargar_matriz_secuencial_ballotage(matriz_ballotage)
                    if matriz_ballotage[0][PORCENTAJE_VOTOS] > matriz_ballotage[1][PORCENTAJE_VOTOS]:
                        print(f" la lista ganadora es la {
                            matriz_ballotage[0][NUMERO_DE_LISTA]}")
                    else:
                        print(f" la lista ganadora es la {
                            matriz_ballotage[1][NUMERO_DE_LISTA]}")
                else:
                    print("no hubo segunda vuelta")

        case "8":
            seguir = input("desea continuar: s/n").lower

    pausar()

print("Fin del programa")
