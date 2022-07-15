#Abriendo el archivo json
import json

#Validacion del json
def json_validator(jsonFile):
    try:
        json.load(jsonFile)
    except ValueError as err:
        print(err)
        return False
    return True

with open('eventos_black.json' , 'r') as archivo:
    datos_del_cliente = json.load(archivo)#Guardo todos los datos del Json en la listadaots_del_cliente
    print("Archivo obtenido correctamente: ",json_validator(archivo))

#datos_del_cliente['nombre']   #Así se llaman a los atributos del JSON, en este caso estoy llamando al atributo nombre

# PARTE CLIENTE DEL UML
class Cliente:
    def __init__(self, nombre, apellido, numero, dni, tipo):
        self.nombre = nombre
        self.apellido = apellido
        self.numero = numero
        self.dni = dni
        self.tipo = tipo
        self.direccion = (datos_del_cliente['direccion']['calle'],datos_del_cliente['direccion']['numero'],datos_del_cliente['direccion']['ciudad'],datos_del_cliente['direccion']['provincia'],datos_del_cliente['direccion']['pais'])

#Creo los metodos
    def puede_crear_chequera(self):
        pass
    def puede_crear_tarjeta_credito(self):
        pass
    def puede_comprar_dolar(self):
        pass
#Metodos creados 

    def __str__(self): #Al mostrar un objeto, se muestra feo, esta linea de codigo hace que se vea más bonito
        return 'Nombre ' + str(self.nombre) + ', apellido: ' + (self.apellido) + ', numero: ' + str(self.numero) + ', dni: ' + str(self.dni) + ', tipo: ' + str(self.tipo)
#Acá creo un objeto cliente llamado c1 y le agrego los atributos de la lista datos_del_cliente
cliente1 = Cliente(datos_del_cliente['nombre'], datos_del_cliente['apellido'], datos_del_cliente['numero'], datos_del_cliente['dni'], datos_del_cliente['tipo'])

# PARTE CUENTA DEL UML
class Cuenta:
    def __init__(self,limite_extraccion_diario, limite_transferencia_recibida, costo_transferencias, saldo_descubierto_disponible):
        self.limite_extraccion_diario = float(limite_extraccion_diario)
        self.limite_transferencia_recibida = float(limite_transferencia_recibida)
        self.costo_transferencias = float(costo_transferencias)
        self.saldo_descubierto_disponible = float(saldo_descubierto_disponible)

if cliente1.tipo == 'CLASSIC':
    cuenta = Cuenta(10000, 150000, 0.1, 0)
elif cliente1.tipo == 'GOLD':
    cuenta = Cuenta(20000, 500000, 0.05, 10000)
elif cliente1.tipo== 'BLACK':
    cuenta = Cuenta(100000, 0, 0, 10000)


#PARTE CLASSIC GOLD Y BLACK

class Classic (Cliente):
    def __init__(self, nombre, apellido, numero, dni, tipo):
        super().__init__(nombre, apellido, numero, dni, tipo)

    def puede_crear_chequera():
        cantidadMaxima= 0
        return cantidadMaxima

    def puede_crear_tarjeta_credito():
        cantidadMaxima= 0
        return cantidadMaxima
    
    def puede_comprar_dolar(self):
        return False

    def verificaciones(self):
        with open('transacciones.html', 'a') as file:  
            for el in datos_del_cliente['transacciones']:
                    if el['estado'] == 'ACEPTADA':
                        agregar_registros = file.writelines(f'<div> <h3>Fecha: {el["fecha"]}</h3> <p>Nombre: {self.nombre}</p> \n <p>Apellido: {self.apellido}</p> <p>Numero: {self.numero}</p> \n <p>Dni: {self.dni}</p> \n <p> Tipo: {el["tipo"]} </p> \n <p> Estado: {el["estado"]} </p> \n <p> Monto: {el["monto"]}')

                    if el['estado'] == 'RECHAZADA' and el['tipo'] == 'RETIRO_EFECTIVO_CAJERO_AUTOMATICO':
                        if el['cupoDiarioRestante'] < el['monto']:
                            agregar_registros = file.writelines(f'<div> <h3>Fecha: {el["fecha"]}</h3> <p>Nombre: {self.nombre}</p> \n <p>Apellido: {self.apellido}</p> <p>Numero: {self.numero}</p> \n <p>Dni: {self.dni}</p> \n <p> Tipo: {el["tipo"]} </p> \n <p> Estado: {el["estado"]} </p> \n <p> Monto: {el["monto"]} <p>Motivo de rechazo: El monto de retiro excede su saldo disponible diario</p>\n')
                        elif el['monto'] > el['saldoEnCuenta']:
                            agregar_registros = file.writelines(f'<div> <h3>Fecha: {el["fecha"]}</h3> <p>Nombre: {self.nombre}</p> \n <p>Apellido: {self.apellido}</p> <p>Numero: {self.numero}</p> \n <p>Dni: {self.dni}</p> \n <p> Tipo: {el["tipo"]} </p> \n <p> Estado: {el["estado"]} </p> \n <p> Monto: {el["monto"]} <p>Motivo de rechazo: El monto de retiro excede su saldo en cuenta</p>\n')
                        
                    elif el['estado'] == 'RECHAZADA' and el['tipo'] == 'ALTA_TARJETA_CREDITO':
                            agregar_registros = file.writelines(f'<div> <h3>Fecha: {el["fecha"]}</h3> <p>Nombre: {self.nombre}</p> \n <p>Apellido: {self.apellido}</p> <p>Numero: {self.numero}</p> \n <p>Dni: {self.dni}</p> \n <p> Tipo: {el["tipo"]} </p> \n <p> Estado: {el["estado"]} </p> \n <p> Monto: {el["monto"]} <p>Motivo de rechazo: Usted no puede solicitar una tarjeta de credito\n')
                        
                    elif el['estado'] == 'RECHAZADA' and el['tipo'] == 'ALTA_CHEQUERA':
                            agregar_registros = file.writelines(f'<div> <h3>Fecha: {el["fecha"]}</h3> <p>Nombre: {self.nombre}</p> \n <p>Apellido: {self.apellido}</p> <p>Numero: {self.numero}</p> \n <p>Dni: {self.dni}</p> \n <p> Tipo: {el["tipo"]} </p> \n <p> Estado: {el["estado"]} </p> \n <p> Monto: {el["monto"]} <p>Motivo de rechazo: Usted no puede solicitar una chequera\n')

                    elif el['estado'] == 'RECHAZADA' and el['tipo'] == 'COMPRA_DOLAR':
                            agregar_registros = file.writelines(f'<div> <h3>Fecha: {el["fecha"]}</h3> <p>Nombre: {self.nombre}</p> \n <p>Apellido: {self.apellido}</p> <p>Numero: {self.numero}</p> \n <p>Dni: {self.dni}</p> \n <p> Tipo: {el["tipo"]} </p> \n <p> Estado: {el["estado"]} </p> \n <p> Monto: {el["monto"]} <p>Motivo de rechazo: Usted no puede comprar dólares\n' )

                    elif el['estado'] == 'RECHAZADA' and el['tipo'] == 'TRANSFERENCIA_ENVIADA':
                        if el['monto'] == el['saldoEnCuenta'] or el['monto'] > el['saldoEnCuenta']:
                            agregar_registros = file.writelines(
                                f'<div> <h3>Fecha: {el["fecha"]}</h3> <p>Nombre: {self.nombre}</p> \n <p>Apellido: {self.apellido}</p> <p>Numero: {self.numero}</p> \n <p>Dni: {self.dni}</p> \n <p> Tipo: {el["tipo"]} </p> \n <p> Estado: {el["estado"]} </p> \n <p> Monto: {el["monto"]} </p> \n <p>Motivo de rechazo: Saldo insuficiente para realizar la transferencia. Acuerdense que se le suma el {cuenta.costo_transferencias}% del monto de la transferencia.\n </div>')

                    elif el['estado'] == 'RECHAZADA' and el['tipo'] == 'TRANSFERENCIA_RECIBIDA': 
                        if el['monto'] > cuenta.limite_transferencia_recibida:
                            agregar_registros = file.writelines(f'<div> <h3>Fecha: {el["fecha"]}</h3> <p>Nombre: {self.nombre}</p> \n <p>Apellido: {self.apellido}</p> <p>Numero: {self.numero}</p> \n <p>Dni: {self.dni}</p> \n <p> Tipo: {el["tipo"]} </p> \n <p> Estado: {el["estado"]} </p> \n <p> Monto: {el["monto"]}<p>Motivo de rechazo: No puede recibir transferencias mayores a {cuenta.limite_transferencia_recibida}\n')



class Gold (Cliente):
    def __init__(self, nombre, apellido, numero, dni, tipo):
        super().__init__(nombre, apellido, numero, dni, tipo)

    def puede_crear_chequera():
        cantidadMaxima= 1
        return cantidadMaxima

    def puede_crear_tarjeta_credito():
        cantidadMaxima= 1
        return cantidadMaxima
    
    def puede_comprar_dolar(self):
        return True

    def verificaciones(self):
        with open('transacciones.html', 'a') as file:  
            for el in datos_del_cliente['transacciones']:
                    if el['estado'] == 'ACEPTADA':
                        agregar_registros = file.writelines(f'<div> <h3>Fecha: {el["fecha"]}</h3> <p>Nombre: {self.nombre}</p> \n <p>Apellido: {self.apellido}</p> <p>Numero: {self.numero}</p> \n <p>Dni: {self.dni}</p> \n <p> Tipo: {el["tipo"]} </p> \n <p> Estado: {el["estado"]} </p> \n <p> Monto: {el["monto"]}')

                    if el['estado'] == 'RECHAZADA' and el['tipo'] == 'RETIRO_EFECTIVO_CAJERO_AUTOMATICO':
                        if el['cupoDiarioRestante'] < el['monto']:
                            agregar_registros = file.writelines(f'<div> <h3>Fecha: {el["fecha"]}</h3> <p>Nombre: {self.nombre}</p> \n <p>Apellido: {self.apellido}</p> <p>Numero: {self.numero}</p> \n <p>Dni: {self.dni}</p> \n <p> Tipo: {el["tipo"]} </p> \n <p> Estado: {el["estado"]} </p> \n <p> Monto: {el["monto"]} <p>Motivo de rechazo: El monto de retiro excede su saldo disponible diario</p>\n')
                        elif el['monto'] > el['saldoEnCuenta']:
                            agregar_registros = file.writelines(f'<div> <h3>Fecha: {el["fecha"]}</h3> <p>Nombre: {self.nombre}</p> \n <p>Apellido: {self.apellido}</p> <p>Numero: {self.numero}</p> \n <p>Dni: {self.dni}</p> \n <p> Tipo: {el["tipo"]} </p> \n <p> Estado: {el["estado"]} </p> \n <p> Monto: {el["monto"]} <p>Motivo de rechazo: El monto de retiro excede su saldo en cuenta</p>\n')
                        
                    elif el['estado'] == 'RECHAZADA' and el['tipo'] == 'ALTA_TARJETA_CREDITO':
                        if Gold.puede_crear_tarjeta_credito() == el['totalTarjetasDeCreditoActualmente']:
                            agregar_registros = file.writelines(f'<div> <h3>Fecha: {el["fecha"]}</h3> <p>Nombre: {self.nombre}</p> \n <p>Apellido: {self.apellido}</p> <p>Numero: {self.numero}</p> \n <p>Dni: {self.dni}</p> \n <p> Tipo: {el["tipo"]} </p> \n <p> Estado: {el["estado"]} </p> \n <p> Monto: {el["monto"]} <p>Motivo de rechazo: El limite de 1 tarjeta de credito ya fue alcanzado\n')
                        
                    elif el['estado'] == 'RECHAZADA' and el['tipo'] == 'ALTA_CHEQUERA':
                        if Gold.puede_crear_chequera() == el['totalChequerasActualmente']:
                            agregar_registros = file.writelines(f'<div> <h3>Fecha: {el["fecha"]}</h3> <p>Nombre: {self.nombre}</p> \n <p>Apellido: {self.apellido}</p> <p>Numero: {self.numero}</p> \n <p>Dni: {self.dni}</p> \n <p> Tipo: {el["tipo"]} </p> \n <p> Estado: {el["estado"]} </p> \n <p> Monto: {el["monto"]} <p>Motivo de rechazo: El limite de 1 chequera ya fue alcanzado\n')

                    elif el['estado'] == 'RECHAZADA' and el['tipo'] == 'COMPRA_DOLAR':
                            agregar_registros = file.writelines(f'<div> <h3>Fecha: {el["fecha"]}</h3> <p>Nombre: {self.nombre}</p> \n <p>Apellido: {self.apellido}</p> <p>Numero: {self.numero}</p> \n <p>Dni: {self.dni}</p> \n <p> Tipo: {el["tipo"]} </p> \n <p> Estado: {el["estado"]} </p> \n <p> Monto: {el["monto"]} <p>Motivo de rechazo: Saldo insuficiente para hacer la compra\n' )

                    elif el['estado'] == 'RECHAZADA' and el['tipo'] == 'TRANSFERENCIA_ENVIADA':
                        if el['monto'] > el['saldoEnCuenta'] or el['monto'] == el['saldoEnCuenta']:
                            agregar_registros = file.writelines(
                                f'<div> <h3>Fecha: {el["fecha"]}</h3> <p>Nombre: {self.nombre}</p> \n <p>Apellido: {self.apellido}</p> <p>Numero: {self.numero}</p> \n <p>Dni: {self.dni}</p> \n <p> Tipo: {el["tipo"]} </p> \n <p> Estado: {el["estado"]} </p> \n <p> Monto: {el["monto"]} </p> \n <p>Motivo de rechazo: Saldo insuficiente para realizar la transferencia. Acuerdense que se le suma el {cuenta.costo_transferencias}% del monto de la transferencia\n </div>')
                    
                    elif el['estado'] == 'RECHAZADA' and el['tipo'] == 'TRANSFERENCIA_RECIBIDA': 
                        if cuenta.limite_transferencia_recibida < el['monto']:
                            agregar_registros = file.writelines(f'<div> <h3>Fecha: {el["fecha"]}</h3> <p>Nombre: {self.nombre}</p> \n <p>Apellido: {self.apellido}</p> <p>Numero: {self.numero}</p> \n <p>Dni: {self.dni}</p> \n <p> Tipo: {el["tipo"]} </p> \n <p> Estado: {el["estado"]} </p> \n <p> Monto: {el["monto"]}<p>Motivo de rechazo: La transferencia es mayor a lo permitido, {cuenta.limite_transferencia_recibida} \n')




class Black (Cliente):
    def __init__(self, nombre, apellido, numero, dni, tipo):
        super().__init__(nombre, apellido, numero, dni, tipo)

    def puede_crear_chequera():
        cantidadMaxima= 2
        return cantidadMaxima

    def puede_crear_tarjeta_credito():
        cantidadMaxima= 5
        return cantidadMaxima

    def puede_comprar_dolar():
        return True

    def retiro_efectivo():
        retiroDiario = 100000
        return retiroDiario

    def transferencias_enviadas():
        pass

    def transferencias_recibidas():
        pass

    def verificaciones(self):
        with open('transacciones.html', 'a') as file:  
            for el in datos_del_cliente['transacciones']:
                    if el['estado'] == 'ACEPTADA':
                        agregar_registros = file.writelines(f'<div> <h3>Fecha: {el["fecha"]}</h3> <p>Nombre: {self.nombre}</p> \n <p>Apellido: {self.apellido}</p> <p>Numero: {self.numero}</p> \n <p>Dni: {self.dni}</p> \n <p> Tipo: {el["tipo"]} </p> \n <p> Estado: {el["estado"]} </p> \n <p> Monto: {el["monto"]}')

                    if el['estado'] == 'RECHAZADA' and el['tipo'] == 'RETIRO_EFECTIVO_CAJERO_AUTOMATICO':
                        if el['cupoDiarioRestante'] < el['monto']:
                            agregar_registros = file.writelines(f'<div> <h3>Fecha: {el["fecha"]}</h3> <p>Nombre: {self.nombre}</p> \n <p>Apellido: {self.apellido}</p> <p>Numero: {self.numero}</p> \n <p>Dni: {self.dni}</p> \n <p> Tipo: {el["tipo"]} </p> \n <p> Estado: {el["estado"]} </p> \n <p> Monto: {el["monto"]} <p>Motivo de rechazo: El monto de retiro excede su saldo disponible diario</p>\n')
                        elif el['monto'] > el['saldoEnCuenta']:
                            agregar_registros = file.writelines(f'<div> <h3>Fecha: {el["fecha"]}</h3> <p>Nombre: {self.nombre}</p> \n <p>Apellido: {self.apellido}</p> <p>Numero: {self.numero}</p> \n <p>Dni: {self.dni}</p> \n <p> Tipo: {el["tipo"]} </p> \n <p> Estado: {el["estado"]} </p> \n <p> Monto: {el["monto"]} <p>Motivo de rechazo: El monto de retiro es mayor al saldo en cuenta</p>\n')

                    elif el['estado'] == 'RECHAZADA' and el['tipo'] == 'ALTA_TARJETA_CREDITO':
                        if Black.puede_crear_tarjeta_credito() == el['totalTarjetasDeCreditoActualmente']:
                            agregar_registros = file.writelines(f'<div> <h3>Fecha: {el["fecha"]}</h3> <p>Nombre: {self.nombre}</p> \n <p>Apellido: {self.apellido}</p> <p>Numero: {self.numero}</p> \n <p>Dni: {self.dni}</p> \n <p> Tipo: {el["tipo"]} </p> \n <p> Estado: {el["estado"]} </p> \n <p> Monto: {el["monto"]} <p>Motivo de rechazo: El limite de 5 tarjetas de credito ya fue alcanzado\n')
                        
                    elif el['estado'] == 'RECHAZADA' and el['tipo'] == 'ALTA_CHEQUERA':
                        if Black.puede_crear_chequera() == el['totalChequerasActualmente']:
                            agregar_registros = file.writelines(f'<div> <h3>Fecha: {el["fecha"]}</h3> <p>Nombre: {self.nombre}</p> \n <p>Apellido: {self.apellido}</p> <p>Numero: {self.numero}</p> \n <p>Dni: {self.dni}</p> \n <p> Tipo: {el["tipo"]} </p> \n <p> Estado: {el["estado"]} </p> \n <p> Monto: {el["monto"]} <p>Motivo de rechazo: El limite de 2 chequeras ya fue alcanzado\n')

                    elif el['estado'] == 'RECHAZADA' and el['tipo'] == 'COMPRA_DOLAR':
                            agregar_registros = file.writelines(f'<div> <h3>Fecha: {el["fecha"]}</h3> <p>Nombre: {self.nombre}</p> \n <p>Apellido: {self.apellido}</p> <p>Numero: {self.numero}</p> \n <p>Dni: {self.dni}</p> \n <p> Tipo: {el["tipo"]} </p> \n <p> Estado: {el["estado"]} </p> \n <p> Monto: {el["monto"]} <p>Motivo de rechazo: Saldo insuficiente para hacer la conversion\n' )

                    elif el['estado'] == 'RECHAZADA' and el['tipo'] == 'TRANSFERENCIA_ENVIADA':
                            agregar_registros = file.writelines(
                                f'<div> <h3>Fecha: {el["fecha"]}</h3> <p>Nombre: {self.nombre}</p> \n <p>Apellido: {self.apellido}</p> <p>Numero: {self.numero}</p> \n <p>Dni: {self.dni}</p> \n <p> Tipo: {el["tipo"]} </p> \n <p> Estado: {el["estado"]} </p> \n <p> Monto: {el["monto"]} </p> \n <p>Motivo de rechazo: Saldo insuficiente para realizar la transferencia\n </div>')


if cliente1.tipo == 'CLASSIC':
    tipoCliente = Classic(datos_del_cliente['nombre'], datos_del_cliente['apellido'], datos_del_cliente['numero'], datos_del_cliente['dni'], datos_del_cliente['tipo'])
elif cliente1.tipo == 'GOLD':
    tipoCliente = Gold(datos_del_cliente['nombre'], datos_del_cliente['apellido'], datos_del_cliente['numero'], datos_del_cliente['dni'], datos_del_cliente['tipo'])
elif cliente1.tipo == 'BLACK':
    tipoCliente = Black(datos_del_cliente['nombre'], datos_del_cliente['apellido'], datos_del_cliente['numero'], datos_del_cliente['dni'], datos_del_cliente['tipo'])
print(tipoCliente.verificaciones())
