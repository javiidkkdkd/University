import matplotlib.pyplot as plt   #Antonella Bravo y Javier Fuentes                             #importa una biblioteca que sirve para la visualizacion de datos en 2d
# Función para leer datos desde el archivo
def lectura_datos():
    archivo = open('universidad\protocolo_vigilancia.txt', 'r', encoding='UTF-8')  #abre el archivo en modo lectura
    datos = []
    for linea in archivo:
        linea = linea.rstrip('\n')
        lista = linea.split(',')
        datos.append(lista)
    archivo.close()
    return datos                                         #devuelve la lista de listas con los datos del archivo


def funcion_a(datos):
    arica = 0
    tarapaca = 0 
    antofagasta = 0
    coquimbo = 0
    valparaiso = 0
    metropolitana = 0 
    ohiggins = 0
    maule = 0
    nuble = 0
    biobio = 0
    araucania = 0
    los_rios = 0 
    los_lagos = 0
    aysen = 0
    magallanes = 0
    
    for lista in datos: 
        if lista[8] == "H5N1":
            if lista[3] == "Arica":
                arica += 1
            elif lista[3] == "Tarapaca":
                tarapaca += 1 
            elif lista[3] == "Antofagasta":
                antofagasta += 1
            elif lista[3] == "Coquimbo":
                coquimbo += 1
            elif lista[3] == "Valparaiso":
                valparaiso += 1
            elif lista[3] == "Metropolitana":
                metropolitana += 1
            elif lista[3] == "O Higgins":
                ohiggins += 1 
            elif lista[3] == "Maule":
                maule += 1
            elif lista[3] == "Nuble":
                nuble += 1
            elif lista[3] == "Bio Bio":
                biobio += 1
            elif lista[3] == "Araucania":
                araucania += 1
            elif lista[3] == "Los Rios":
                los_rios += 1
            elif lista[3] == "Los Lagos":
                los_lagos += 1
            elif lista[3] == "Aysen":
                aysen += 1
            elif lista[3] == "Magallanes":
                magallanes += 1
            lista2 = [arica, tarapaca, antofagasta, coquimbo, valparaiso, metropolitana, ohiggins, maule, nuble, biobio, araucania, los_rios, los_lagos, aysen, magallanes]
    return lista2
    
# Función para contar casos negativos en abril de 2023 

def funcion_b(datos):                         
    conteo = 0                                                 #inicializa un contador para contar los casos
    for fila in datos:                                         #se repite el proceso sobre cada fila en la lista de datos proporcionados
        fecha = fila[2]
        clasificacion = fila[9].lower()                    #obtiene la clasificacion de la fila 8 y las convierte en minusculas 
        if "04-2023" in fecha and clasificacion == "negativo":
            conteo += 1                                    #incrementa el contador si la fecha es "04-2023" y la clasificación es "negativo"
    return conteo                                              #devuelve el numero total de casos de negativos en abril 2023

# Función para contar casos negativos de la especie "Yunco" 
def funcion_c(datos): 
    conteo = 0
    for fila in datos:
        especie = fila[5]
        clasificacion = fila[9].lower()
        if "Yunco" in especie and clasificacion == "negativo":
            conteo += 1
    return conteo

# Función para contar incidencias del "Lile" en junio de 2023
def funcion_d(datos):
    conteo = 0
    for fila in datos:
        fecha = fila[2]
        especie = fila[5]
        clasificacion = fila[9].lower()
        if "06-2023" in fecha and "Lile" in especie and clasificacion == "negativo":
            conteo += 1
    return conteo

# Función para graficar el gráfico de barras
def funcion_e(datos):
    especies = ["Gaviota", "Piquero", "Salteador", "Pelicano", "Guanay"]
    conteo= funcion_g(datos)
    plt.bar(especies, conteo)
    plt.title("Protocolo de Vigilancia - Casos Negativos por Especie")
    plt.xlabel("Especies")
    plt.ylabel("Casos Negativos")
    for i, count in enumerate(conteo):                                        #añadir los valores exactos sobre las barras
        plt.text(i, count + 0.1, str(count), ha="center", va="bottom")
    plt.show()

# Función auxiliar para contar casos negativos de una especie específica
def funcion_g(datos):
    gaviota = 0
    piquero = 0
    salteador = 0
    pelicano = 0
    guanay = 0

    for lista in datos:
        if (lista[9]) == "Negativo":
            if "Gaviota" in (lista[5]):
                gaviota += 1
            elif "Piquero" in (lista[5]):
                piquero += 1 
            elif "Salteador" in (lista[5]):
                salteador += 1
            elif "Pelicano" in (lista[5]):
                pelicano += 1
            elif "Guanay" in (lista[5]):
                guanay += 1
        especies =[gaviota, piquero, salteador, pelicano, guanay]
    return especies
    # Escribir resultados en un archivo de texto

def generar_salida(datos):
    archivo2 = open("resultadoS3.txt", 'w', encoding='UTF-8') #crea el un archivo .txt
    archivo2.write("Antonella Bravo - Javier Fuentes\n") #integrantes
    archivo2.write("\n") #espacio en blanco
    archivo2.write("Cantidad de casos de secuenciacion por region:") #escribe en el archivo txt las regiones y la cantidad de casos por region en las que haya h5n1
    archivo2.write("\n") #espacio en blanco
    regiones = ["Arica", "Tarapaca", "Antofagasta", "Coquimbo", "Valparaiso", "Metropolitana", "Ohiggins", "Maule", "Nuble", "Biobio", "Araucania", "Los_Rios", "Los_Lagos", "Aysen", "Magallanes"]
    resultados_regiones = funcion_a(datos)
    for i in range(len(regiones)):
        archivo2.write(f"{regiones[i]}: {resultados_regiones[i]}\n")
    archivo2.write("\n") 
    archivo2.write(f"Casos negativos en abril de 2023: {funcion_b(datos)}\n") #escribe en el archivo txt los casos negativos del 06/2023
    archivo2.write("\n") 
    archivo2.write(f"Casos negativos de la especie Yunco: {funcion_c(datos)}\n") #escribe en el archivo txt los casos negativos de Yunco
    archivo2.write("\n") 
    archivo2.write(f"Incidencias en junio de 2023 del 'Lile': {funcion_d(datos)}") #escribe en el archivo txt los casos negativos de Lile
    archivo2.close()


if __name__ == "__main__":
    datos = lectura_datos()
    resultados_H5N1 = funcion_a(datos) #respuesta al punto a de la tarea
    resultados_abril_2023 = funcion_b(datos) #respuesta al punto b de la tarea
    resultados_yunco = funcion_c(datos) #respuesta al punto c de la tarea
    resultados_lile_junio_2023 = funcion_d(datos) #respuesta al punto d de la tarea
    grafico_de_barras = funcion_e(datos) #respuesta al punto e de la tarea
    generar_salida(datos)