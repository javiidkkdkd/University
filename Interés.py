#Javier Fuentes
#VF = VA * (1 + i) ** n
#VA = VF/(1 + i) ** n

#Imprime los valores futuros por cada año
def calcular_valor_futuro(capital, interes, years):
    print("VALOR FUTURO")
    for n in range(years + 1):  #desde año 0 hasta years
        vf = capital * (1 + interes) ** n  #fórmula del valor futuro
        print(f"Año {n}: {vf}")
    return vf

#Imprime los valores actuales por cada año
def calcular_valor_actual(capital_futuro, interes, years):
    print("\nVALOR ACTUAL")
    for n in range(years + 1):  #desde año 0 hasta 'anios'
        va = capital_futuro / (1 + interes) ** n  #fórmula del valor actual
        print(f"Año {n}: {va}")
    return va

#salida
if __name__ == "__main__":
    capital_inicial = float(input("Ingrese el capital inicial (en unidades monetarias): "))    #pide al usuario el capital inicial
    tasa_interes = float(input("Ingrese la tasa de interés anual (sin '%'): ")) / 100 #pide al usuario la tasa de interés como porcentaje y la convierte a decimal
    years = int(input("Ingrese el número de años: "))   #pide al usuario el número de años
    #llamada de las funciones
    calcular_valor_futuro(capital_inicial, tasa_interes, years)
    calcular_valor_actual(capital_inicial, tasa_interes, years)
