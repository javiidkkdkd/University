#Antonella Bravo y Javier Fuentes
#funcion para leer los datos en el archivo de texto
def lectura_datos():
    archivo = open('en_palabras.txt', 'r', encoding='ASCII') #abre el archivo en modo lectura
    lineas = archivo.readlines()
    archivo.close() 
    return [linea.strip() for linea in lineas] #devuelve una lista con las lineas sin espacios

#diccionario para las palabras requeridas
numeros = {"zero": 0, "one": 1 , "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10, "eleven": 11, "twelve": 12, "thirteen": 13, "fourteen": 14, "fifteen": 15, "sixteen": 16, "eighteen": 18, "nineteen": 19, "twenty": 20, "thirty": 30, "fourty": 40, "fifty": 50, "sixty": 60, "seventy": 70, "eighty": 80, "ninety": 90}
#diccionario para los multiplicadores
multiplos = {"million": 1000000, "thousand": 1000, "hundred": 100} 

#convertir palabras a numeros
def pal_num(letras):
    letras = letras.replace(',', '')
    letras = letras.replace('-', ' ')
    
    letras = letras.lower()  #pasa de mayusculas a minusculas
    letras = letras.split()  #separa las palabras
    
    total = 0 
    conteo = 0 
    negative = False
    
    for letra in letras:
        if letra == "negative":
            negative = True 
        elif letra in numeros:  
            conteo += numeros[letra] 
        elif letra in multiplos:
            
            if conteo == 0:
                conteo = 1  
            
            conteo *= multiplos[letra]
        if letra == "thousand" or letra == "million":  #si encuentra estas palabras, se lo suma al total y reinicia el conteo
            total += conteo
            conteo = 0
    
    total += conteo
    
    if negative:
        total = -total 

    return total

#creacion del archivo
def archivo_salida(lineas):
    archivo2 = open('en_numeros.txt', 'w', encoding='ASCII') #crea el un archivo .txt
    archivo2.write("Antonella Bravo - Javier Fuentes\n") #integrantes
    archivo2.write("\n") #espacio en blanco
    for linea in lineas:
        if linea == "": 
            archivo2.write("\n")  
        else:
            numero = pal_num(linea) #separa las lineas
            archivo2.write(f"{numero}\n") #escribe el numero de la suma 
    archivo2.close()

if __name__ == "__main__":
    lineas = lectura_datos()
    archivo_salida(lineas)