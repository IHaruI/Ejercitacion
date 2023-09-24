import funciones
import entretenimiento
import os
import sys

lista_numeros = []
lista_palabras = []

# Se ha realizado con fines de entretimiento.

def limpiado_de_pantalla():
        os.system("pause")
        os.system("cls")

def agregado_de_numeros():
    print("Ingrese la cantidad de numeros que desea. (0 para salir.)")
    
    while True:
        try:
            numero = int(input("Ingrese un número: "))
                    
            if numero != 0:
                lista_numeros.append(int(numero))
            else:
                break
        except:    
            print("Error, ingrese solo números.")

while True:
    try:
        print("|¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯|")
        print("|     ----- ¡Bienvenido! -----     |")
        print("|――――――――――――――――――――――――――――――――――|")
        print("|         Menu de Opciones         |")
        print("|――――――――――――――――――――――――――――――――――|")
        print("|1. Calcular área de un círaculo.  |")
        print("|2. Verificar par o impar.         |")
        print("|3. Sumar cantidad de números.     |")
        print("|4. Encontrar número maxímo.       |")
        print("|5. Devolver palabras invertidas.  |")
        print("|6. Ordenar listas de palabras.    |")
        print("|7. Calcular potencia de un número.|")
        print("|8. Devolver solo numero pares.    |")
        print("|9. Calcular productos de números. |")
        print("|10. Determinar si es palíndromo.  |")
        print("|0. Para salir.                    |")
        print("|__________________________________|")
        opcion = int(input("Opción elegida: "))
        os.system("cls")
        
        match opcion:
            case 1:
                entretenimiento.circulo(funciones.calcular_area_circulo(float(input('Ingrese el área del ciculo: '))))
                #print(f"El área del circulo es: {funciones.calcular_area_circulo(float(input('Ingrese el área del ciculo: '))):.2f}")
                limpiado_de_pantalla()
            case 2:
                numero = input("Ingrese un número: ")

                if numero.isdigit():
                    entretenimiento.par_impar(funciones.validar_par_o_impar(int(numero)))
                    #print(f"El número es: {funciones.validar_par_o_impar(int(numero))}")
                    limpiado_de_pantalla()
                else:
                    print("Error, ingrese solo números.")
                    limpiado_de_pantalla()
            case 3:
                agregado_de_numeros()
                entretenimiento.suma_de_lista(funciones.suma_de_datos(lista_numeros))
                #print(f"La suma de todos los números ingresados es: {funciones.suma_de_datos(lista_numeros)}")
                lista_numeros.clear()
                limpiado_de_pantalla()
            case 4:
                while True:
                    try:
                        numero1 = int(input("Ingrese el 1er número: "))
                        numero2 = int(input("Ingrese el 2do número: "))
                        numero3 = int(input("Ingrese el 3er número: "))
                        break
                    except:
                        print("Error, ingrese solo números.")
                
                entretenimiento.numero_mayor(funciones.numero_maximo(numero1, numero2, numero3))
                #print(f"El número maximo de los tres es: {funciones.numero_maximo(numero1, numero2, numero3)}")
                limpiado_de_pantalla()
            case 5:
                entretenimiento.invercion(funciones.invertir_cadena(input('Ingrese una palabra: ')))
                #print(f"La palabra invertida es: {funciones.invertir_cadena(input('Ingrese una palabra: '))}")
                limpiado_de_pantalla()
            case 6:
                print("Ingrese la cantidad de palabras que desea. ('s' para salir.)")
                while True:
                    palabra = input("Ingrese una palabra: ")

                    if palabra.isalpha() and palabra.lower() != "s":
                        lista_palabras.append(palabra)
                    elif palabra.lower() == "s":
                        break
                    else:
                        print("Error, ingrese solo letras.")

                entretenimiento.listado_ordenado(funciones.lista_ordenada(lista_palabras))
                #print(f"El ordenamiento alfabéticamente es: {funciones.lista_ordenada(lista_palabras)}")
                limpiado_de_pantalla()
            case 7:
                try:
                    base = int(input("Ingrese la base: "))
                    exponente = int(input("Ingrese el exponente: "))
                    entretenimiento.base_e_exponente(funciones.calcular_potencia(base, exponente))
                    #print(f"La potencia es: {funciones.calcular_potencia(base, exponente)}")
                    limpiado_de_pantalla()
                except:
                    print("Error, ingrese solo numeros.")
                    limpiado_de_pantalla()
            case 8:
                agregado_de_numeros()
                entretenimiento.numeros_pares(funciones.lista_de_solo_pares(lista_numeros))
                #print(f"Los números pares son: {funciones.lista_de_solo_pares(lista_numeros)}")
                lista_numeros.clear()
                limpiado_de_pantalla()
            case 9:
                agregado_de_numeros()
                entretenimiento.producto(funciones.calcular_prodcuto(lista_numeros))
                #print(f"El producto de los números ingresados es: {funciones.calcular_prodcuto(lista_numeros)}")
                lista_numeros.clear()
                limpiado_de_pantalla()
            case 10:
                entretenimiento.palindromo(funciones.validar_palindromo(input('Ingrese una palabra: ')))
                #print(f"La palabra ingresada: {funciones.validar_palindromo(input('Ingrese una palabra: '))}")
                limpiado_de_pantalla()
            case 0:
                entretenimiento.saitama()
                os.system("pause")
                sys.exit()
    except ValueError:
        print("Error, Eliga una de las opciones!")
        os.system("pause")
        os.system("cls")