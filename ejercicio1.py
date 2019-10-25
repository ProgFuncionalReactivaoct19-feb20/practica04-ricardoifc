import codecs
import json
# importo codecs y json
archivo = codecs.open("datos.txt", "r")
lineas = archivo.readlines()
# en lineas saco las cadenas de cada linea del archivo
lineas_diccionario = [json.loads(l) for l in lineas]
# convierto cada cadena en un diccionario

# valido los goles mayor a 3 con un lambda y en la posicion 1,1
validarGoles = lambda x: list(x.items())[1][1] > 3
print("Goles mayores a 3:")
# en una lista filtro tomando el diccionario
print(list(filter(validarGoles, lineas_diccionario)))

print("Paises de Nigeria:")
# filtro todos los que lleven el pais de nigeria
validarPais = lambda x: list(x.items())[0][1] == "Nigeria"
# ahora mando un filtro con el diccionario
print(list(filter(validarPais, lineas_diccionario)))

print("Valor minimo y valor maximo:")
# saco la lista en posicion 2,1
validarEstatura =lambda x: list(x.items())[2][1]
# uso min y max para despues imprimirlos
print("minimo:")
print(min(list(map(validarEstatura, lineas_diccionario))))
print("maximo:")
print(max(list(map(validarEstatura, lineas_diccionario))))