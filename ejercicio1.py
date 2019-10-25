import codecs
import json

archivo = codecs.open("datos.txt", "r")
lineas = archivo.readlines()
# linea_diccionario = json.loads(lineas[0])
lineas_diccionario = [json.loads(l) for l in lineas]

validarGoles = lambda x: list(x.items())[1][1] > 3
print("Goles mayores a 3:")
print(list(filter(validarGoles, lineas_diccionario)))



print("Paises de Nigeria:")
validarPais = lambda x: list(x.items())[0][1] == "Nigeria"
print(list(filter(validarPais, lineas_diccionario)))

print("Valor minimo y valor maximo:")
validarEstatura = lambda x: list(x.items())[2][1]
print(min(validarEstatura, lineas_diccionario))
print(max(validarEstatura, lineas_diccionario))