#Desarrollar una función que reciba dos diccionarios como paráametros y los mezcle, es decir,
#que se construya un nuevo diccionario con las llaves de los dos diccionarios; si hay una clave repetida en ambos diccionarios,
#se debe asignar el valor que tenga la clave en el primer diccionario.

#Función para mezclar dos diccionarios.
def mezclar_diccionarios (diccionario1:dict,diccionario2:dict)->dict:
    diccionario2.update(diccionario1) #Actualiza el diccionario 2 con los elementos del diccionario 1- (Como es el diccionario 2 el que se actualiza, si hay claves repetidas, se toma la del primer diccionario).
    return diccionario2 #Devuelve el diccionario 2 actualizado (Ya con los elementos del diccionario 1).
if __name__ == "__main__":
    diccionario_frutas = {1: "manzana", 2: "naranja", 3: "pera", 4: "uva", 5: "banano", 6: "fresa", 7: "sandía", 8: "mango", 9: "piña", 10: "durazno"} #Diccionario 1.
    diccionario_animales = {11: "león", 12: "tigre", 2: "elefante", 5: "jirafa", 7: "rinoceronte", 13: "cebra", 1: "canguro", 14: "oso", 10: "lobo", 15: "águila"} #Diccionario 2.
    mezcla=mezclar_diccionarios(diccionario1 = diccionario_frutas, diccionario2 = diccionario_animales) #Llama a la función para mezclar ambos diccionarios-
    llaves=mezcla.keys() #Obtiene las llaves del diccionario mezclado.
    for l in llaves:
        print(f"{l}: {mezcla[l]}") #Imprime cada clave con su valor asociado del diccionario mezclado.