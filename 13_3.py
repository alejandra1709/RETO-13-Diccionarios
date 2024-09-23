#Cree un programa que lea de un archivo con dicho JSON y:
#Imprima los nombres completos (nombre y apellidos) de las personas que practican el deporte ingresado por el usuario.
#Imprima los nombres completos (nombre y apellidos) de las personas que esten en un rango de edades dado por el usuario.


import json

#Función que busca personas que parctican un deporte.
def nombres_deporte (diccionario:dict, deporte:str):
    for k,v in diccionario.items(): #Se recorre el diccionario.
        if deporte in v['deportes']: #Si el deporte ingresado está en la lista de deportes de la persona...
            print(f"{v['nombres']} {v['apellidos']}") #Se imprime el nombre y apellido de la persona.

#Función que busca personas que están en un rango de edad.
def nombres_rango_edad (diccionario:dict, minima:int, maxima:int):
    for k,v in diccionario.items(): #Se recorre el diccionario.
        if minima <= v['edad'] <= maxima: #Si la edad de la persona es mayor al mínimo especificado y menor al máximo específicado...
            print(f"{v['nombres']} {v['apellidos']}") #Se imprime el nombre y apellido de la persona.

if __name__ == "__main__":
    juan_dorotea = "C:\\Users\\aleja\\OneDrive\\Escritorio\\juan_dorotea.json" #Ubicación archivo JSON.
    readFile = open(juan_dorotea, "r") #Abre el archivo JSON en modo lectura.
    data = json.load(readFile) #Convierte ek¿l contenido del archivo en un diccionario.
    readFile.close() #Cierra el archivo después de leerlo.

    deporte = input("Escriba un deporte a consultar entre Futbol, Ajedrez, Gimnasia y Baloncesto: ") #Solicita al usuario ingresar un deporte.
    if deporte=="Futbol" or deporte=="Ajedrez" or deporte=="Gimnasia" or deporte =="Baloncesto": 
        nombres_deporte(diccionario=data,deporte=deporte) #Si el deporte es válido, se llama a la función para buscar quién lo practica.
    else:
        print("Escriba un deporte válido (Primera letra debe estar en mayúscula)") #Sino se solicita escribir un deporte válido.

    edad_min = int(input("Ingrese la edad mínima a consultar: ")) #Se solicita al usuario ingresar un rango de edad.
    edad_max = int(input("Ingrese la edad máxima a consultar: "))
    nombres_rango_edad(diccionario=data,minima=edad_min,maxima=edad_max) #Se llama a la función para buscar las personas que están en ese rango de edad.
