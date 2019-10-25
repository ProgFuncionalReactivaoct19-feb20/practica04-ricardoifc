import codecs
import json

archivo = codecs.open("datos.txt", "r")
lineas = archivo.readlines()
# print(len(lineas))
# print(lineas[0])
# diccionario ={"provincia": "Pichincha", "capital": "Quito", "cantones": 20}
# print(list(diccionario.keys()))
# print(list(diccionario.item()))[0][0]
# print(lineas[0])
linea_diccionario = json.loads(lineas[0])
# print(linea_diccionario)
lineas_diccionario = [json.loads(l) for l in lineas]
# print(lineas_diccionario[0])
funcion = lambda x: list(x.items())[2][1]
print(list(map(funcion, lineas_diccionario)))