

estudiantes = {
    "Ana": [8, 9, 7, 10],
    "Julia": [8, 9, 7, 10],
    "Adriana": [8, 9, 7, 10],
    "Benjamín": [8, 9, 7, 10],
    "Diego": [8, 9, 7, 10], 
    "Juan": [8, 9, 7, 10], 
    "María": [9, 10, 9, 8],
    "Pedro": [7, 8, 6, 9]
}
print(f"                   {'estudiante':>12}  {'promedio':>10} {'max':>5} {'min':>5}")
print("-------------------------------------------------------------------------------")
#funcion para calcular el promedio del estudiante
for clave, valores in estudiantes.items():
    suma_valores = sum(valores)
    promedio = suma_valores/len(valores)
#funcion para calcular nota maxima
    nota_max = max(valores)
#funcion para calcular nota minima
    nota_min = min(valores)
#funcion para imprimir los resultados
    print(f"El promedio de {clave:>12} es: {promedio:>10.2f} {nota_max:>5} {nota_min:>5}") 