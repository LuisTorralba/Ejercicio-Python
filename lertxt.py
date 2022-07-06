import requests
import os

def openFile(path):
    try:
        print("Leyendo archivo...")
        archivo = open(path)
        lista = []
        for linea in archivo:
            datos = linea.strip().split(",")
            lista.append(datos)
        archivo.close()
        print("Archivo leído con éxito.")
        return lista
    except IOError as e:
        print("El archivo no existe. {}".format(e))

def enviaInsert():
    try:
        datos = openFile("archivo/empleados.txt");
        for i in datos:
            empleados = {"nombre" : i[0], "apellido" : i[1],
                        "country" : {"nombre" : i[2],
                                     "airport" : [{"nombre": i[4]}]},
                        "likedLenguajes": [{"nombre" : i[3]}]}
            print("Enviando petición...")
            resp = requests.post("http://localhost:8080/empleados/apiv1/clientes/add", json=empleados)
            print("Petición realizada con éxito.")
            print(resp)
            print(resp.json())
    except requests.exceptions.RequestException as e:
        print("Error en la petición: {}".format(e))

enviaInsert()