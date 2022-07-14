#Abriendo el archivo json
import json
with open('eventos_black.json' , 'r') as archivo:
    datos_del_cliente = json.load(archivo)#Guardo todos los datos del Json en la listadaots_del_cliente
    print("Archivo obtenido con exito")
#FALTA VALIDAR QUE EL JSON ESTÉ BIEN
#datos_del_cliente['nombre']   #Así se llaman a los atributos del JSON, en este caso estoy llamando al atributo nombre


# PARTE CLIENTE DEL UML
#Creando Constructor
class Cliente:
    def __init__(Clientes, nombre, apellido, numero, dni):
        Cliente.nombre = nombre
        Cliente.apellido = apellido
        Cliente.numero = numero
        Cliente.dni = dni
#Constructor terminado y creado

#Creo los metodos
    def puede_crear_chequera(Clientes):
        Cliente.aceptado=True
    def puede_crear_tarjeta_credito(Clientes):
        Cliente._aceptado = True
    def puede_comprar_dolar(Clientes):
        Cliente._aceptado = True
#Metodos creados 

    def __str__(Cliente): #Al mostrar un objeto, se muestra feo, esta linea de codigo hace que se vea más bonito
        return 'Nombre ' + str(Cliente.nombre) + ', apellido: ' + (Cliente.apellido) + ', numero: ' + str(Cliente.numero) + ', dni: ' + str(Cliente.dni)
#Acá creo un objeto cliente llamado c1 y le agrego los atributos de la lista datos_del_cliente
cliente1 = Cliente(datos_del_cliente['nombre'], datos_del_cliente['apellido'], datos_del_cliente['numero'], datos_del_cliente['dni'])
print(c1)
#PARTE CLASSIC GOLD Y BLACK
class Classic (Cliente):
    Cliente.aceptado=False
    pass
class Gold (Cliente):
    Cliente.aceptado=False
    pass
class Black (Cliente):
    Cliente.aceptado=False
    pass 

# PARTE CUENTA DEL UML
#Creando Constructor
class Cuenta:
    def __init__(Cuentas,limite_extraccion_diario, limite_transferencia_recibida, monto, costo_transferencias, saldo_descubierto_disponible):
        Cuentas.limite_extraccion_diario = limite_extraccion_diario
        Cuentas.limite_transferencia_recibida = limite_transferencia_recibida
        Cuentas.monto = monto
        Cuentas.costo_transferencias = costo_transferencias
        Cuentas.saldo_descubierto_disponible = saldo_descubierto_disponible
#cuenta1 = Cuenta(datos_del_cliente['nombre'])
# PARTE CUENTA DEL UML
#Creando Constructor
class Direccion:
    def __init__(Cuentas,calle,numero,ciudad,provincia,pais):
        Direccion.calle=calle
        Direccion.numero=numero
        Direccion.ciudad=ciudad
        Direccion.provincia=provincia
        Direccion.pais=pais