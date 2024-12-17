#Javier Fuentes
import random

#genera una figura respetando las probabilidades indicadas
def generar_figura():
    numeros = {
        7: 0.02,  # 2% probabilidad
        6: 0.03,  # 3% probabilidad
        5: 0.05,  # 5% probabilidad
        4: 0.10,  # 10% probabilidad
        3: 0.10,  # 10% probabilidad
        2: 0.20,  # 20% probabilidad
        1: 0.20,  # 20% probabilidad
        0: 0.30   # 30% probabilidad
    }
    figuras = list(numeros.keys()) #crea lista de los numeros
    probabilidades = list(numeros.values()) #crea lisa de las probabilidades
    return random.choices(figuras, probabilidades, k=1)[0] #elige una figura dependiendo de las probabilidades

#Calcula el premio en base a las figuras/numeros obtenidas/os
def calcular_apuesta(figuras, apuesta):
    if figuras.count(7) == 3:
        return apuesta * 1000
    elif figuras.count(7) == 2:
        return apuesta * 10
    elif figuras.count(6) == 2:
        return apuesta * 10
    elif figuras.count(5) == 2:
        return apuesta * 10
    elif figuras.count(7) == 1:
        return apuesta * 5
    elif figuras.count(6) == 3:
        return apuesta * 250
    elif figuras.count(5) == 3:
        return apuesta * 150
    elif figuras.count(4) == 3:
        return apuesta * 50
    elif figuras.count(3) == 3:
        return apuesta * 50
    elif figuras.count(2) == 3:
        return apuesta * 30
    elif figuras.count(1) == 3:
        return apuesta * 30
    elif figuras.count(0) == 3:
        return apuesta * 20
    else:
        return 0
    
#Función principal para simular el tragamonedas.
def tragamonedas():
    saldo = int(input("Ingrese el monto inicial: "))
    
    for _ in range(10000):
        if saldo < 100:
            print("Saldo insuficiente. Intente de nuevo.")
            break

        print(f"Saldo actual: ${saldo}")
        apuesta = int(input("Ingrese su apuesta ($100, $500, $1000): "))
        if apuesta not in [100, 500, 1000]:
            print("Apuesta no válida. Intente de nuevo.")
            continue
        if apuesta > saldo:
            print("Saldo insuficiente. Intente de nuevo.")
            continue

        # Generar las figuras
        figuras = [generar_figura() for _ in range(3)]
        print("Figuras obtenidas:", " - ".join(map(str, figuras))) #convierte cada numero en la lista figuras en una cadena de texto separandose con un -

        # Calcular el premio
        premio = calcular_apuesta(figuras, apuesta)
        if premio > 0:
            print(f"¡Ganaste! Premio: ${premio}")
            saldo += premio
        else:
            print(f"Perdiste la apuesta de ${apuesta}")
            saldo -= apuesta

        # Verificar si el jugador desea continuar
        continuar = input("¿Desea continuar? (1=SI, 0=NO): ")
        if continuar != "1":
            break

    print(f"Saldo final: ${saldo}")
    print("Gracias por jugar.")

# Ejecutar el programa
if __name__ == "__main__":
    tragamonedas()
