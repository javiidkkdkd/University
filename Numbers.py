#Antonella Bravo y Javier Fuentes

#diccionario para las palabras requeridas
numeros = {"zero": 0, "one": 1 , "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10, "eleven": 11, "twelve": 12, "thirteen": 13, "fourteen": 14, "fifteen": 15, "sixteen": 16, "eighteen": 18, "nineteen": 19, "twenty": 20, "thirty": 30, "fourty": 40, "fifty": 50, "sixty": 60, "seventy": 70, "eighty": 80, "ninety": 90, "hundred": 100}

multiplos = {"thousand": 1000, "million": 1000000}

#lectura de datos
def lectura_datos():
    archivo = open('en_palabras.txt', 'r', encoding='UTF-8')  #abre el archivo en modo lectura
    datos = []
    for linea in archivo:
        linea = linea.rstrip('\n')
        lista = linea.split(' ')
        datos.append(lista)
    archivo.close()
    return datos  

#convertir palabras a numeros
def pal_num(pal):
    pal = pal.split()
    total = 0 
    conteo = 0
    negative = False
    
    for word in pal:
        if word == "negative":
            negative = True
        elif word in numeros:
            conteo += numeros[word]
        elif word == "hundred":
            conteo *= 100
        elif word in multiplos:
            total += conteo * multiplos[word]
            conteo = 0

    total += conteo
    return -total if negative else total 

def generar_salida(datos):
    archivo2 = open("en_numeros.txt", 'w', encoding='UTF-8') #crea el un archivo .txt
    archivo2.write("Antonella Bravo - Javier Fuentes\n") #integrantes
    archivo2.write("\n") #espacio en blanco
    archivo2.write(f"{pal_num(datos)}\n") #escribe en el archivo txt los casos negativos de Yunco
    archivo2.write("\n") 
    archivo2.close()