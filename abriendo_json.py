import json
#datos_del_cliente['nombre']   #Así se llaman a los atributos del JSON, en este caso estoy llamando al atributo nombre

try:
    with open('eventos_classic.json' , 'r') as archivo:
        datos_del_cliente = json.load(archivo)#Guardo todos los datos del Json en la lista datos_del_cliente
        print("Archivo obtenido con exito")
except FileNotFoundError as err:
    print("Archivo no encontrado")
    quit()