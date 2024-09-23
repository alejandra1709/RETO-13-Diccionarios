# Desarrollar un algoritmo que imprima de manera ascendente los valores (todos del mismo tipo) de un diccionario.

#Función que recibe un diccionario y devuelve una lista con los valores del diccionario en orden ascendente.
def valores_ascendentes (codigo_colores:dict)->list:
    valores=(list(codigo_colores.values())) #Extrae los valores del diccionario en una lista.
    valores_ordenados=sorted(valores) #Ordena los valores de la lista en orden ascendente.
    return valores_ordenados #Devuelve la lista con los valores del diccionario ordenados.

if __name__ == "__main__":
    codigo_colores = {"gris":8,"verde":5,"negro":0,"azul":6,"rojo":2,"amarillo":4,"cafe":1,"blanco":9,"violeta":7,"naranja":3} #Diccionario código de colores resistencias, colores cómo llaves y números como valores.
    valores_asc=valores_ascendentes(codigo_colores) #Llama a la función para obtener los valores del diccionario ordenados.
    for i in valores_asc:
        print (i) #Se imprimen los valores del diccionario en orden.