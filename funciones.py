import math

# ---------------------------------------------------------------------------------
def calcular_area_circulo(radio) -> float:
    return math.pi * pow(radio, 2)
# ---------------------------------------------------------------------------------
def validar_par_o_impar(numero):
    if (numero % 2 == 0):
        return "Es par"
    else:
        return "Es impar"
# ---------------------------------------------------------------------------------
def suma_de_datos(lista):
    acumulador = 0

    for dato in lista:
        acumulador = acumulador + dato
    
    return acumulador
# ---------------------------------------------------------------------------------
def numero_maximo(numero1, numero2, numero3):
    mayor = 0

    if numero1 > numero2 and numero1 > numero3:
        mayor = numero1
    elif numero2 > numero1 and numero2 > numero3:
        mayor = numero2
    else:
        mayor = numero3

    return mayor
# ---------------------------------------------------------------------------------
def invertir_cadena(cadena):
    cadenaInvertida = ""

    for letra in cadena:
        cadenaInvertida = letra + cadenaInvertida

    return cadenaInvertida

#     return cadena[::-1]
# ---------------------------------------------------------------------------------
def lista_ordenada(lista):
    return sorted(lista)
# ---------------------------------------------------------------------------------
def calcular_potencia(base, exponente):
    return pow(base, exponente)
# ---------------------------------------------------------------------------------
def lista_de_solo_pares(lista):
    lista_de_pares = []

    for i in lista:
        if (i % 2 == 0):
            lista_de_pares.append(i)
    
    return lista_de_pares
# ---------------------------------------------------------------------------------
def calcular_prodcuto(lista):
    resultado = 1

    for i in lista:
        resultado = i * resultado
    
    return resultado
# ---------------------------------------------------------------------------------
def validar_palindromo(cadena):
    
    inicio = 0
    fin = len(cadena) - 1

    while cadena[inicio] == cadena[fin]:
        
        if inicio >= fin:
            return "Es palíndromo"
        
        inicio = inicio + 1
        fin = fin - 1
    
    return "No es palíndromo"
# ---------------------------------------------------------------------------------