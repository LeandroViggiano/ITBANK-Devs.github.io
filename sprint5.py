import cliente_y_cuenta
import classic_black_y_gold
#Abriendo el archivo json
import json
#datos_del_cliente['nombre']   #Así se llaman a los atributos del JSON, en este caso estoy llamando al atributo nombre

try:
    with open('eventos_gold.json' , 'r') as archivo:
        datos_del_cliente = json.load(archivo)#Guardo todos los datos del Json en la lista datos_del_cliente
        print("Archivo obtenido con exito")
except FileNotFoundError as err:
    print("Archivo no encontrado")
    quit()


#Acá creo un objeto cliente llamado c1 y le agrego los atributos de la lista datos_del_cliente


classic_black_y_gold.Classic

classic_black_y_gold.Gold

classic_black_y_gold.Black

if cliente_y_cuenta.cliente1.tipo == 'CLASSIC':
    tipoCliente = classic_black_y_gold.Classic(datos_del_cliente['nombre'], datos_del_cliente['apellido'], datos_del_cliente['numero'], datos_del_cliente['dni'], datos_del_cliente['tipo'])
elif cliente_y_cuenta.cliente1.tipo == 'GOLD':
    tipoCliente = classic_black_y_gold.Gold(datos_del_cliente['nombre'], datos_del_cliente['apellido'], datos_del_cliente['numero'], datos_del_cliente['dni'], datos_del_cliente['tipo'])
elif cliente_y_cuenta.cliente1.tipo == 'BLACK':
    tipoCliente = classic_black_y_gold.Black(datos_del_cliente['nombre'], datos_del_cliente['apellido'], datos_del_cliente['numero'], datos_del_cliente['dni'], datos_del_cliente['tipo'])
print(tipoCliente.verificaciones()) 

