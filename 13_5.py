#A través de un programa conectese a al menos 3 API's , obtenga el JSON, imprimalo y extraiga los pares de llave : valor.

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
