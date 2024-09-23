# RETO 13 - diccionarios
>***1. Desarrollar un algoritmo que imprima de manera ascendente los valores (todos del mismo tipo) de un diccionario.***
```python
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
```
>***2. Desarrollar una función que reciba dos diccionarios como parámetros y los mezcle, es decir, que se construya un nuevo diccionario con las llaves de los dos diccionarios; si hay una clave repetida en ambos diccionarios, se debe asignar el valor que tenga la clave en el primer diccionario.***
```python
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
```
>***3. Dado el JSON:
```python
{
	"jadiazcoronado":{
		"nombres": "Juan Antonio",
		"apellidos": "Diaz Coronado",
		"edad":19,
		"colombiano":true,
		"deportes":["Futbol","Ajedrez","Gimnasia"]
	},
	"dmlunasol":{
		"nombres": "Dorotea Maritza",
		"apellidos": "Luna Sol",
		"edad":25,
		"colombiano":false,
		"deportes":["Baloncesto","Ajedrez","Gimnasia"]
	}
}
```
>***Cree un programa que lea de un archivo con dicho JSON y:***

> * Imprima los nombres completos (nombre y apellidos) de las personas que practican el deporte ingresado por el usuario.
> * Imprima los nombres completos (nombre y apellidos) de las personas que esten en un rango de edades dado por el usuario.
```python
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
```
>***4. El siguiente código contiene un JSON con el pronostivo detallado del clima para 8 días:***
```python
import json

# Cargar archivo
jsonString = '''
{\"dt\": {\"0\": 1685116800, \"1\": 1685203200, \"2\": 1685289600, \"3\": 1685376000, \"4\": 1685462400, \"5\": 1685548800, \"6\": 1685635200, \"7\": 1685721600}, \"sunrise\": {\"0\": 1685097348, \"1\": 1685183745, \"2\": 1685270143, \"3\": 1685356542, \"4\": 1685442942, \"5\": 1685529342, \"6\": 1685615743, \"7\": 1685702145}, \"sunset\": {\"0\": 1685143042, \"1\": 1685229458, \"2\": 1685315875, \"3\": 1685402291, \"4\": 1685488708, \"5\": 1685575124, \"6\": 1685661541, \"7\": 1685747958}, \"moonrise\": {\"0\": 1685118300, \"1\": 1685207460, \"2\": 1685296620, \"3\": 1685385720, \"4\": 1685474880, \"5\": 1685564220, \"6\": 1685653740, \"7\": 1685743500}, \"moonset\": {\"0\": 0, \"1\": 1685164320, \"2\": 1685253000, \"3\": 1685341560, \"4\": 1685430120, \"5\": 1685518740, \"6\": 1685607600, \"7\": 1685696640}, \"moon_phase\": {\"0\": 0.22, \"1\": 0.25, \"2\": 0.28, \"3\": 0.31, \"4\": 0.35, \"5\": 0.38, \"6\": 0.41, \"7\": 0.45}, \"pressure\": {\"0\": 1011, \"1\": 1012, \"2\": 1012, \"3\": 1012, \"4\": 1012, \"5\": 1012, \"6\": 1012, \"7\": 1011}, \"humidity\": {\"0\": 85, \"1\": 61, \"2\": 68, \"3\": 74, \"4\": 84, \"5\": 66, \"6\": 81, \"7\": 82}, \"dew_point\": {\"0\": 23.93, \"1\": 22.5, \"2\": 23.67, \"3\": 23.35, \"4\": 24.22, \"5\": 22.73, \"6\": 23.18, \"7\": 22.93}, \"velViento\": {\"0\": 3.56, \"1\": 5.07, \"2\": 5.38, \"3\": 3.95, \"4\": 4.74, \"5\": 3.75, \"6\": 4.08, \"7\": 5.94}, \"dirViento\": {\"0\": 188, \"1\": 14, \"2\": 21, \"3\": 23, \"4\": 40, \"5\": 330, \"6\": 176, \"7\": 168}, \"wind_gust\": {\"0\": 6.47, \"1\": 8.86, \"2\": 8.95, \"3\": 6.12, \"4\": 7.17, \"5\": 5.4, \"6\": 5.13, \"7\": 9.67}, \"weather\": {\"0\": [{\"id\": 501, \"main\": \"Rain\", \"description\": \"lluvia moderada\", \"icon\": \"10d\"}], \"1\": [{\"id\": 500, \"main\": \"Rain\", \"description\": \"lluvia ligera\", \"icon\": \"10d\"}], \"2\": [{\"id\": 501, \"main\": \"Rain\", \"description\": \"lluvia moderada\", \"icon\": \"10d\"}], \"3\": [{\"id\": 500, \"main\": \"Rain\", \"description\": \"lluvia ligera\", \"icon\": \"10d\"}], \"4\": [{\"id\": 501, \"main\": \"Rain\", \"description\": \"lluvia moderada\", \"icon\": \"10d\"}], \"5\": [{\"id\": 500, \"main\": \"Rain\", \"description\": \"lluvia ligera\", \"icon\": \"10d\"}], \"6\": [{\"id\": 500, \"main\": \"Rain\", \"description\": \"lluvia ligera\", \"icon\": \"10d\"}], \"7\": [{\"id\": 500, \"main\": \"Rain\", \"description\": \"lluvia ligera\", \"icon\": \"10d\"}]}, \"clouds\": {\"0\": 100, \"1\": 82, \"2\": 99, \"3\": 100, \"4\": 100, \"5\": 59, \"6\": 100, \"7\": 100}, \"pop\": {\"0\": 1.0, \"1\": 0.65, \"2\": 0.98, \"3\": 0.86, \"4\": 1.0, \"5\": 0.62, \"6\": 0.93, \"7\": 0.95}, \"prcp\": {\"0\": 40.0, \"1\": 1.65, \"2\": 14.01, \"3\": 5.07, \"4\": 16.55, \"5\": 2.17, \"6\": 2.77, \"7\": 1.73}, \"uvi\": {\"0\": 10.14, \"1\": 12.78, \"2\": 12.73, \"3\": 8.44, \"4\": 0.59, \"5\": 1.0, \"6\": 1.0, \"7\": 1.0}, \"temp.day\": {\"0\": 26.62, \"1\": 30.95, \"2\": 30.17, \"3\": 28.37, \"4\": 27.22, \"5\": 29.78, \"6\": 26.83, \"7\": 26.36}, \"tmpMin\": {\"0\": 25.64, \"1\": 24.64, \"2\": 25.84, \"3\": 25.56, \"4\": 25.72, \"5\": 24.86, \"6\": 25.96, \"7\": 25.47}, \"tmpMax\": {\"0\": 27.16, \"1\": 31.1, \"2\": 30.2, \"3\": 29.5, \"4\": 28.87, \"5\": 29.78, \"6\": 28.96, \"7\": 28.25}, \"temp.night\": {\"0\": 25.67, \"1\": 27.39, \"2\": 26.24, \"3\": 27.2, \"4\": 25.92, \"5\": 27.14, \"6\": 26.56, \"7\": 25.66}, \"temp.eve\": {\"0\": 25.91, \"1\": 28.73, \"2\": 27.42, \"3\": 28.27, \"4\": 27.94, \"5\": 29.29, \"6\": 28.96, \"7\": 28.12}, \"temp.morn\": {\"0\": 26.5, \"1\": 24.64, \"2\": 26.13, \"3\": 25.72, \"4\": 26.04, \"5\": 24.86, \"6\": 25.98, \"7\": 25.57}, \"feels_like.day\": {\"0\": 26.62, \"1\": 34.99, \"2\": 34.96, \"3\": 32.03, \"4\": 30.67, \"5\": 33.62, \"6\": 29.45, \"7\": 26.36}, \"feels_like.night\": {\"0\": 26.56, \"1\": 30.98, \"2\": 26.24, \"3\": 30.62, \"4\": 26.84, \"5\": 30.16, \"6\": 26.56, \"7\": 26.45}, \"feels_like.eve\": {\"0\": 26.85, \"1\": 32.49, \"2\": 30.94, \"3\": 31.8, \"4\": 31.51, \"5\": 33.17, \"6\": 32.64, \"7\": 31.18}, \"feels_like.morn\": {\"0\": 26.5, \"1\": 25.48, \"2\": 26.13, \"3\": 26.62, \"4\": 26.04, \"5\": 25.73, \"6\": 25.98, \"7\": 26.4}, \"date\": {\"0\": 1685098800000, \"1\": 1685185200000, \"2\": 1685271600000, \"3\": 1685358000000, \"4\": 1685444400000, \"5\": 1685530800000, \"6\": 1685617200000, \"7\": 1685703600000}, \"main\": {\"0\": \"Rain\", \"1\": \"Rain\", \"2\": \"Rain\", \"3\": \"Rain\", \"4\": \"Rain\", \"5\": \"Rain\", \"6\": \"Rain\", \"7\": \"Rain\"}, \"description\": {\"0\": \"lluvia moderada\", \"1\": \"lluvia ligera\", \"2\": \"lluvia moderada\", \"3\": \"lluvia ligera\", \"4\": \"lluvia moderada\", \"5\": \"lluvia ligera\", \"6\": \"lluvia ligera\", \"7\": \"lluvia ligera\"}, \"icono\": {\"0\": \"10d\", \"1\": \"10d\", \"2\": \"10d\", \"3\": \"10d\", \"4\": \"10d\", \"5\": \"10d\", \"6\": \"10d\", \"7\": \"10d\"}, \"alertPrecip\": {\"0\": \"X\", \"1\": \"-\", \"2\": \"-\", \"3\": \"-\", \"4\": \"-\", \"5\": \"-\", \"6\": \"-\", \"7\": \"-\"}, \"alertAlertas\": {\"0\": \"-\", \"1\": \"-\", \"2\": \"-\", \"3\": \"-\", \"4\": \"-\", \"5\": \"-\", \"6\": \"-\", \"7\": \"-\"}, \"alertVelViento\": {\"0\": \"-\", \"1\": \"-\", \"2\": \"X\", \"3\": \"-\", \"4\": \"-\", \"5\": \"-\", \"6\": \"-\", \"7\": \"-\"}, \"alertTmpMax\": {\"0\": \"-\", \"1\": \"-\", \"2\": \"-\", \"3\": \"-\", \"4\": \"-\", \"5\": \"X\", \"6\": \"-\", \"7\": \"-\"}, \"alertTmpMin\": {\"0\": \"-\", \"1\": \"X\", \"2\": \"-\", \"3\": \"-\", \"4\": \"-\", \"5\": \"-\", \"6\": \"-\", \"7\": \"-\"}, \"recomendaciones\": {\"lluvias\": \"Realice una revisi\\u00f3n y limpieza a la red de desague y canales existentes ENTER8 Cuente con una estaci\\u00f3n de bombeo, que debe estar ubicada en el punto m\\u00e1s bajo del predio. Aseg\\u00farese de encender y probar el sistema de bombeo al menos una vez al mes y hacer un mantenimiento mensual al equipo de bombeoENTER8 Los productos alojados en zonas de almacenamiento deben mantenersen sobre estibas - estanterias, con el fin de que no entren en contacto directo con el agua.\", \"vientos\": \"-\", \"temperatura\": \"-\"}}
'''
data = json.loads(jsonString)
```
> Revise los campos: 'alertAlertas', 'alertPrecip', 'alertTmpMax', 'alertTmpMin', 'alertVelViento'. Para cada uno identifique si se presentan alertas ({0: x} indica que el día 0 habra un fenomeno de la alerta en cuestión, {1:"-"} indica que no habrá ningun fenomeno climatico). En caso que se presente una alerta obtenga la fecha del campo 'dt' (aquí pueden revisar como se convierte de UTC a fecha), así como los parametros relevantes del evento (e.g. si es un fenomeno de lluvias, busque el nivel de lluvia, si es vientos, la velocidad del viento). Al final deberá imprimir las fechas de alerta, el tipo de alerta y las variables asociadas.
```python
import json
from datetime import datetime

# Función para convertir una fecha en formato UTC a un formato día-mes-año.
def convertir_fecha(UTC):
    return datetime.utcfromtimestamp(UTC).strftime('%d-%m-%Y') # Convierte el tiempo UTC a formato de fecha (día-mes-año)

# Función para verificar y procesar alertas.
def revisar_alerta(alertas, tipo_alerta, parametro, data, dt_field, extra_param=None):
    # Recorre todas las alertas del JSON.
    for dia, alerta in alertas.items():
        if alerta == "X":  # Si existe una alerta ('X')...
            fecha = convertir_fecha(data[dt_field][dia])  # Obtiene la fecha en formato legible.
            # Imprimir el tipo de alerta y su respectivo parámnetro.
            if extra_param:
                print(f"Alerta de {tipo_alerta} el {fecha}: {parametro} = {data[parametro][dia]} {extra_param} = {data[extra_param][dia]}")
            else:
                print(f"Alerta de {tipo_alerta} el {fecha}: {parametro} = {data[parametro][dia]}")

# Cargar el archivo JSON
jsonString = '''
{\"dt\": {\"0\": 1685116800, \"1\": 1685203200, \"2\": 1685289600, \"3\": 1685376000, \"4\": 1685462400, \"5\": 1685548800, \"6\": 1685635200, \"7\": 1685721600}, \"sunrise\": {\"0\": 1685097348, \"1\": 1685183745, \"2\": 1685270143, \"3\": 1685356542, \"4\": 1685442942, \"5\": 1685529342, \"6\": 1685615743, \"7\": 1685702145}, \"sunset\": {\"0\": 1685143042, \"1\": 1685229458, \"2\": 1685315875, \"3\": 1685402291, \"4\": 1685488708, \"5\": 1685575124, \"6\": 1685661541, \"7\": 1685747958}, \"moonrise\": {\"0\": 1685118300, \"1\": 1685207460, \"2\": 1685296620, \"3\": 1685385720, \"4\": 1685474880, \"5\": 1685564220, \"6\": 1685653740, \"7\": 1685743500}, \"moonset\": {\"0\": 0, \"1\": 1685164320, \"2\": 1685253000, \"3\": 1685341560, \"4\": 1685430120, \"5\": 1685518740, \"6\": 1685607600, \"7\": 1685696640}, \"moon_phase\": {\"0\": 0.22, \"1\": 0.25, \"2\": 0.28, \"3\": 0.31, \"4\": 0.35, \"5\": 0.38, \"6\": 0.41, \"7\": 0.45}, \"pressure\": {\"0\": 1011, \"1\": 1012, \"2\": 1012, \"3\": 1012, \"4\": 1012, \"5\": 1012, \"6\": 1012, \"7\": 1011}, \"humidity\": {\"0\": 85, \"1\": 61, \"2\": 68, \"3\": 74, \"4\": 84, \"5\": 66, \"6\": 81, \"7\": 82}, \"dew_point\": {\"0\": 23.93, \"1\": 22.5, \"2\": 23.67, \"3\": 23.35, \"4\": 24.22, \"5\": 22.73, \"6\": 23.18, \"7\": 22.93}, \"velViento\": {\"0\": 3.56, \"1\": 5.07, \"2\": 5.38, \"3\": 3.95, \"4\": 4.74, \"5\": 3.75, \"6\": 4.08, \"7\": 5.94}, \"dirViento\": {\"0\": 188, \"1\": 14, \"2\": 21, \"3\": 23, \"4\": 40, \"5\": 330, \"6\": 176, \"7\": 168}, \"wind_gust\": {\"0\": 6.47, \"1\": 8.86, \"2\": 8.95, \"3\": 6.12, \"4\": 7.17, \"5\": 5.4, \"6\": 5.13, \"7\": 9.67}, \"weather\": {\"0\": [{\"id\": 501, \"main\": \"Rain\", \"description\": \"lluvia moderada\", \"icon\": \"10d\"}], \"1\": [{\"id\": 500, \"main\": \"Rain\", \"description\": \"lluvia ligera\", \"icon\": \"10d\"}], \"2\": [{\"id\": 501, \"main\": \"Rain\", \"description\": \"lluvia moderada\", \"icon\": \"10d\"}], \"3\": [{\"id\": 500, \"main\": \"Rain\", \"description\": \"lluvia ligera\", \"icon\": \"10d\"}], \"4\": [{\"id\": 501, \"main\": \"Rain\", \"description\": \"lluvia moderada\", \"icon\": \"10d\"}], \"5\": [{\"id\": 500, \"main\": \"Rain\", \"description\": \"lluvia ligera\", \"icon\": \"10d\"}], \"6\": [{\"id\": 500, \"main\": \"Rain\", \"description\": \"lluvia ligera\", \"icon\": \"10d\"}], \"7\": [{\"id\": 500, \"main\": \"Rain\", \"description\": \"lluvia ligera\", \"icon\": \"10d\"}]}, \"clouds\": {\"0\": 100, \"1\": 82, \"2\": 99, \"3\": 100, \"4\": 100, \"5\": 59, \"6\": 100, \"7\": 100}, \"pop\": {\"0\": 1.0, \"1\": 0.65, \"2\": 0.98, \"3\": 0.86, \"4\": 1.0, \"5\": 0.62, \"6\": 0.93, \"7\": 0.95}, \"prcp\": {\"0\": 40.0, \"1\": 1.65, \"2\": 14.01, \"3\": 5.07, \"4\": 16.55, \"5\": 2.17, \"6\": 2.77, \"7\": 1.73}, \"uvi\": {\"0\": 10.14, \"1\": 12.78, \"2\": 12.73, \"3\": 8.44, \"4\": 0.59, \"5\": 1.0, \"6\": 1.0, \"7\": 1.0}, \"temp.day\": {\"0\": 26.62, \"1\": 30.95, \"2\": 30.17, \"3\": 28.37, \"4\": 27.22, \"5\": 29.78, \"6\": 26.83, \"7\": 26.36}, \"tmpMin\": {\"0\": 25.64, \"1\": 24.64, \"2\": 25.84, \"3\": 25.56, \"4\": 25.72, \"5\": 24.86, \"6\": 25.96, \"7\": 25.47}, \"tmpMax\": {\"0\": 27.16, \"1\": 31.1, \"2\": 30.2, \"3\": 29.5, \"4\": 28.87, \"5\": 29.78, \"6\": 28.96, \"7\": 28.25}, \"temp.night\": {\"0\": 25.67, \"1\": 27.39, \"2\": 26.24, \"3\": 27.2, \"4\": 25.92, \"5\": 27.14, \"6\": 26.56, \"7\": 25.66}, \"temp.eve\": {\"0\": 25.91, \"1\": 28.73, \"2\": 27.42, \"3\": 28.27, \"4\": 27.94, \"5\": 29.29, \"6\": 28.96, \"7\": 28.12}, \"temp.morn\": {\"0\": 26.5, \"1\": 24.64, \"2\": 26.13, \"3\": 25.72, \"4\": 26.04, \"5\": 24.86, \"6\": 25.98, \"7\": 25.57}, \"feels_like.day\": {\"0\": 26.62, \"1\": 34.99, \"2\": 34.96, \"3\": 32.03, \"4\": 30.67, \"5\": 33.62, \"6\": 29.45, \"7\": 26.36}, \"feels_like.night\": {\"0\": 26.56, \"1\": 30.98, \"2\": 26.24, \"3\": 30.62, \"4\": 26.84, \"5\": 30.16, \"6\": 26.56, \"7\": 26.45}, \"feels_like.eve\": {\"0\": 26.85, \"1\": 32.49, \"2\": 30.94, \"3\": 31.8, \"4\": 31.51, \"5\": 33.17, \"6\": 32.64, \"7\": 31.18}, \"feels_like.morn\": {\"0\": 26.5, \"1\": 25.48, \"2\": 26.13, \"3\": 26.62, \"4\": 26.04, \"5\": 25.73, \"6\": 25.98, \"7\": 26.4}, \"date\": {\"0\": 1685098800000, \"1\": 1685185200000, \"2\": 1685271600000, \"3\": 1685358000000, \"4\": 1685444400000, \"5\": 1685530800000, \"6\": 1685617200000, \"7\": 1685703600000}, \"main\": {\"0\": \"Rain\", \"1\": \"Rain\", \"2\": \"Rain\", \"3\": \"Rain\", \"4\": \"Rain\", \"5\": \"Rain\", \"6\": \"Rain\", \"7\": \"Rain\"}, \"description\": {\"0\": \"lluvia moderada\", \"1\": \"lluvia ligera\", \"2\": \"lluvia moderada\", \"3\": \"lluvia ligera\", \"4\": \"lluvia moderada\", \"5\": \"lluvia ligera\", \"6\": \"lluvia ligera\", \"7\": \"lluvia ligera\"}, \"icono\": {\"0\": \"10d\", \"1\": \"10d\", \"2\": \"10d\", \"3\": \"10d\", \"4\": \"10d\", \"5\": \"10d\", \"6\": \"10d\", \"7\": \"10d\"}, \"alertPrecip\": {\"0\": \"X\", \"1\": \"-\", \"2\": \"-\", \"3\": \"-\", \"4\": \"-\", \"5\": \"-\", \"6\": \"-\", \"7\": \"-\"}, \"alertAlertas\": {\"0\": \"-\", \"1\": \"-\", \"2\": \"-\", \"3\": \"-\", \"4\": \"-\", \"5\": \"-\", \"6\": \"-\", \"7\": \"-\"}, \"alertVelViento\": {\"0\": \"-\", \"1\": \"-\", \"2\": \"X\", \"3\": \"-\", \"4\": \"-\", \"5\": \"-\", \"6\": \"-\", \"7\": \"-\"}, \"alertTmpMax\": {\"0\": \"-\", \"1\": \"-\", \"2\": \"-\", \"3\": \"-\", \"4\": \"-\", \"5\": \"X\", \"6\": \"-\", \"7\": \"-\"}, \"alertTmpMin\": {\"0\": \"-\", \"1\": \"X\", \"2\": \"-\", \"3\": \"-\", \"4\": \"-\", \"5\": \"-\", \"6\": \"-\", \"7\": \"-\"}, \"recomendaciones\": {\"lluvias\": \"Realice una revisi\\u00f3n y limpieza a la red de desague y canales existentes ENTER8 Cuente con una estaci\\u00f3n de bombeo, que debe estar ubicada en el punto m\\u00e1s bajo del predio. Aseg\\u00farese de encender y probar el sistema de bombeo al menos una vez al mes y hacer un mantenimiento mensual al equipo de bombeoENTER8 Los productos alojados en zonas de almacenamiento deben mantenersen sobre estibas - estanterias, con el fin de que no entren en contacto directo con el agua.\", \"vientos\": \"-\", \"temperatura\": \"-\"}}
'''
# Convertir el JSON a diccionario de Python
data = json.loads(jsonString)

# Revisar alertas de precipitación
revisar_alerta(data['alertPrecip'], 'precipitación', 'prcp', data, 'dt')
# Revisar alertas de viento
revisar_alerta(data['alertVelViento'], 'viento', 'velViento', data, 'dt')
# Revisar alertas de temperatura máxima
revisar_alerta(data['alertTmpMax'], 'temperatura máxima', 'tmpMax', data, 'dt')
# Revisar alertas de temperatura mínima
revisar_alerta(data['alertTmpMin'], 'temperatura mínima', 'tmpMin', data, 'dt')
```
>***5. A través de un programa conectese a al menos 3 API's , obtenga el JSON, imprimalo y extraiga los pares de llave : valor.***
```python
import json
import requests

# Función para imprimir pares clave : valor
def imprimir_pares(data):
    for key, value in data.items(): #Itera sobre los elementos del diccionario.
        print(f"{key}: {value}") #Imprime cada clave con su respectivo valor.

# API 1: Precios de criptomonedas
cripto_url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum&vs_currencies=usd"
cripto_response = requests.get(cripto_url) #Realiza la solicitud get a la API.
if cripto_response.status_code == 200: #Se verifica si hubo una respuesta exitosa.
    cripto_data = cripto_response.json() #Convierte la respuesta en un diccionario de python.
    print("Datos de la API CoinGecko (Precios de criptomonedas):")
    (cripto_data) #Llama a la función para imrpimir los datos de la API.
else:
    print(f"Error al acceder a CoinGecko API") #Mensaje de error, por si la solicitud falla.

# API 2: Cantidad de habitantes de los países más poblados.
poblacion_url = "https://restcountries.com/v3.1/all"
poblacion_response = requests.get(poblacion_url) #Realiza la solicitud get a la API.
if poblacion_response.status_code == 200: #Se verifica si hubo una respuesta exitosa.
    poblacion_data = poblacion_response.json() #Convierte la respuesta en un diccionario de python.
    print("Datos de la API REST Countries (Población de los países más poblados):")
    # Ordena los países por población en orden descendente
    sorted_countries = sorted(poblacion_data, key=lambda x: x.get('population', 0), reverse=True)
    for country in sorted_countries[:5]:  # Imprime los 5 países más poblados
        print(f"{country['name']['common']}: {country['population']}")
else:
    print(f"Error al acceder a REST Countries API") #Mensaje de error, por si la solicitud falla.

# API 3: Imagen aleatoria de perros
dog_url = "https://dog.ceo/api/breeds/image/random"
dog_response = requests.get(dog_url) #Realiza la solicitud get a la API.
if dog_response.status_code == 200: #Se verifica si hubo una respuesta exitosa.
    dog_data = dog_response.json() #Convierte la respuesta en un diccionario de python.
    print("Datos de la API Dog CEO's (Imagen aleatoria de perros):")
    imprimir_pares(dog_data) #Llama a la función para imrpimir los datos de la API.
else:
    print(f"Error al acceder a Dog CEO API") #Mensaje de error, por si la solicitud falla.

```
