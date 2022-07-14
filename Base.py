#Abriendo el archivo json
import json
with open('eventos_classic.json' , 'r') as archivo:
    datos_del_cliente = json.load(archivo)#Guardo todos los datos del Json en la listadaots_del_cliente
    print("Archivo obtenido con exito")
#FALTA VALIDAR QUE EL JSON ESTÉ BIEN
#datos_del_cliente['nombre']   #Así se llaman a los atributos del JSON, en este caso estoy llamando al atributo nombre


# PARTE CLIENTE DEL UML
class Cliente:
    def __init__(Clientes, nombre, apellido, numero, dni, tipo):
        Cliente.nombre = nombre
        Cliente.apellido = apellido
        Cliente.numero = numero
        Cliente.dni = dni
        Cliente.tipo = tipo
        Cliente.direccion = (datos_del_cliente['direccion']['calle'],datos_del_cliente['direccion']['numero'],datos_del_cliente['direccion']['ciudad'],datos_del_cliente['direccion']['provincia'],datos_del_cliente['direccion']['pais'])

#Creo los metodos
    def puede_crear_chequera(Clientes):
        pass
    def puede_crear_tarjeta_credito(Clientes):
        pass
    def puede_comprar_dolar(Clientes):
        pass
#Metodos creados 

    def __str__(Cliente): #Al mostrar un objeto, se muestra feo, esta linea de codigo hace que se vea más bonito
        return 'Nombre ' + str(Cliente.nombre) + ', apellido: ' + (Cliente.apellido) + ', numero: ' + str(Cliente.numero) + ', dni: ' + str(Cliente.dni) + ', tipo: ' + str(Cliente.tipo)
#Acá creo un objeto cliente llamado c1 y le agrego los atributos de la lista datos_del_cliente
cliente1 = Cliente(datos_del_cliente['nombre'], datos_del_cliente['apellido'], datos_del_cliente['numero'], datos_del_cliente['dni'], datos_del_cliente['tipo'])

#PARTE CLASSIC GOLD Y BLACK

if Cliente.tipo == 'CLASSIC':    
    class Classic (Cliente):
        def __init__(Cliente, nombre, apellido, numero, dni, tipo):
            super().__init__(nombre, apellido, numero, dni, tipo)

        def puede_crear_chequera(Clientes):
            return False

        def puede_crear_tarjeta_credito(Clientes):
            return False
        
        def puede_comprar_dolar(Clientes):
            return False

        def verificaciones(Clientes):
            with open('transacciones.html', 'a') as file:
                agregar_registros = file.write(f'css')                  

            for el in datos_del_cliente['transacciones']:
                with open('transacciones.html', 'a') as file:  
                    if el['estado'] == 'ACEPTADA':
                        agregar_registros = file.writelines(f'<div> <h3>Fecha: {el["fecha"]}</h3> <p>Nombre: {Cliente.nombre}</p> \n <p>Apellido: {Cliente.apellido}</p> <p>Numero: {Cliente.numero}</p> \n <p>Dni: {Cliente.dni}</p> \n <p> Tipo: {el["tipo"]} </p> \n <p> Estado: {el["estado"]} </p> \n <p> Monto: {el["monto"]}')

                    if el['estado'] == 'RECHAZADA' and el['tipo'] == 'RETIRO_EFECTIVO_CAJERO_AUTOMATICO':
                        if el['cupoDiarioRestante'] < el['monto']:
                            agregar_registros = file.writelines(f'<div> <h3>Fecha: {el["fecha"]}</h3> <p>Nombre: {Cliente.nombre}</p> \n <p>Apellido: {Cliente.apellido}</p> <p>Numero: {Cliente.numero}</p> \n <p>Dni: {Cliente.dni}</p> \n <p> Tipo: {el["tipo"]} </p> \n <p> Estado: {el["estado"]} </p> \n <p> Monto: {el["monto"]} <p>Motivo de rechazo: El monto de retiro excede su saldo disponible diario</p>\n')
                        elif el['monto'] > el['saldoEnCuenta']:
                            agregar_registros = file.writelines(f'<div> <h3>Fecha: {el["fecha"]}</h3> <p>Nombre: {Cliente.nombre}</p> \n <p>Apellido: {Cliente.apellido}</p> <p>Numero: {Cliente.numero}</p> \n <p>Dni: {Cliente.dni}</p> \n <p> Tipo: {el["tipo"]} </p> \n <p> Estado: {el["estado"]} </p> \n <p> Monto: {el["monto"]} <p>Motivo de rechazo: El monto de retiro excede su saldo en cuenta</p>\n')
                        
                    elif el['estado'] == 'RECHAZADA' and el['tipo'] == 'ALTA_TARJETA_CREDITO':
                            agregar_registros = file.writelines(f'<div> <h3>Fecha: {el["fecha"]}</h3> <p>Nombre: {Cliente.nombre}</p> \n <p>Apellido: {Cliente.apellido}</p> <p>Numero: {Cliente.numero}</p> \n <p>Dni: {Cliente.dni}</p> \n <p> Tipo: {el["tipo"]} </p> \n <p> Estado: {el["estado"]} </p> \n <p> Monto: {el["monto"]} <p>Motivo de rechazo: El limite de 1 tarjeta de credito ya fue alcanzado\n')
                        
                    elif el['estado'] == 'RECHAZADA' and el['tipo'] == 'ALTA_CHEQUERA':
                            agregar_registros = file.writelines(f'<div> <h3>Fecha: {el["fecha"]}</h3> <p>Nombre: {Cliente.nombre}</p> \n <p>Apellido: {Cliente.apellido}</p> <p>Numero: {Cliente.numero}</p> \n <p>Dni: {Cliente.dni}</p> \n <p> Tipo: {el["tipo"]} </p> \n <p> Estado: {el["estado"]} </p> \n <p> Monto: {el["monto"]} <p>Motivo de rechazo: El limite de 1 chequera ya fue alcanzado\n')

                    elif el['estado'] == 'RECHAZADA' and el['tipo'] == 'COMPRA_DOLAR':
                            agregar_registros = file.writelines(f'<div> <h3>Fecha: {el["fecha"]}</h3> <p>Nombre: {Cliente.nombre}</p> \n <p>Apellido: {Cliente.apellido}</p> <p>Numero: {Cliente.numero}</p> \n <p>Dni: {Cliente.dni}</p> \n <p> Tipo: {el["tipo"]} </p> \n <p> Estado: {el["estado"]} </p> \n <p> Monto: {el["monto"]} <p>Motivo de rechazo: Saldo insuficiente para hacer la conversion\n' )

                    elif el['estado'] == 'RECHAZADA' and el['tipo'] == 'TRANSFERENCIA_ENVIADA':
                        if el['monto'] > el['cupoDiarioRestante']:
                            agregar_registros = file.writelines(
                                f'<div> <h3>Fecha: {el["fecha"]}</h3> <p>Nombre: {Cliente.nombre}</p> \n <p>Apellido: {Cliente.apellido}</p> <p>Numero: {Cliente.numero}</p> \n <p>Dni: {Cliente.dni}</p> \n <p> Tipo: {el["tipo"]} </p> \n <p> Estado: {el["estado"]} </p> \n <p> Monto: {el["monto"]} </p> \n <p>Motivo de rechazo: Excedio el limite diario \n </div>')
                        elif el['monto'] > el['saldoEnCuenta']:
                            agregar_registros = file.writelines(
                                f'<div> <h3>Fecha: {el["fecha"]}</h3> <p>Nombre: {Cliente.nombre}</p> \n <p>Apellido: {Cliente.apellido}</p> <p>Numero: {Cliente.numero}</p> \n <p>Dni: {Cliente.dni}</p> \n <p> Tipo: {el["tipo"]} </p> \n <p> Estado: {el["estado"]} </p> \n <p> Monto: {el["monto"]} </p> \n <p>Motivo de rechazo: Saldo insuficiente para realizar la transferencia\n </div>')
                    elif el['estado'] == 'RECHAZADA' and el['tipo'] == 'TRANSFERENCIA_RECIBIDA': agregar_registros = file.writelines(f'<div> <h3>Fecha: {el["fecha"]}</h3> <p>Nombre: {Cliente.nombre}</p> \n <p>Apellido: {Cliente.apellido}</p> <p>Numero: {Cliente.numero}</p> \n <p>Dni: {Cliente.dni}</p> \n <p> Tipo: {el["tipo"]} </p> \n <p> Estado: {el["estado"]} </p> \n <p> Monto: {el["monto"]}<p>Motivo de rechazo: La transferencia no fue autorizada \n')

    clienteClassic = Classic(datos_del_cliente['nombre'], datos_del_cliente['apellido'], datos_del_cliente['numero'], datos_del_cliente['dni'], datos_del_cliente['tipo'])

    print(clienteClassic.verificaciones())

if cliente1.tipo == 'GOLD':
    class Gold (Cliente):
        def __init__(Cliente, nombre, apellido, numero, dni, tipo):
            super().__init__(nombre, apellido, numero, dni, tipo)

        def puede_crear_chequera(Clientes):
            return True

        def puede_crear_tarjeta_credito(Clientes):
            return True
        
        def puede_comprar_dolar(Clientes):
            return True

        def verificaciones(Clientes):
            with open('transacciones.html', 'a') as file:
                agregar_registros = file.write(f'css')                  

            for el in datos_del_cliente['transacciones']:
                with open('transacciones.html', 'a') as file:  
                    if el['estado'] == 'ACEPTADA':
                        agregar_registros = file.writelines(f'<div> <h3>Fecha: {el["fecha"]}</h3> <p>Nombre: {Cliente.nombre}</p> \n <p>Apellido: {Cliente.apellido}</p> <p>Numero: {Cliente.numero}</p> \n <p>Dni: {Cliente.dni}</p> \n <p> Tipo: {el["tipo"]} </p> \n <p> Estado: {el["estado"]} </p> \n <p> Monto: {el["monto"]}')

                    if el['estado'] == 'RECHAZADA' and el['tipo'] == 'RETIRO_EFECTIVO_CAJERO_AUTOMATICO':
                        if el['cupoDiarioRestante'] < el['monto']:
                            agregar_registros = file.writelines(f'<div> <h3>Fecha: {el["fecha"]}</h3> <p>Nombre: {Cliente.nombre}</p> \n <p>Apellido: {Cliente.apellido}</p> <p>Numero: {Cliente.numero}</p> \n <p>Dni: {Cliente.dni}</p> \n <p> Tipo: {el["tipo"]} </p> \n <p> Estado: {el["estado"]} </p> \n <p> Monto: {el["monto"]} <p>Motivo de rechazo: El monto de retiro excede su saldo disponible diario</p>\n')
                        elif el['monto'] > el['saldoEnCuenta']:
                            agregar_registros = file.writelines(f'<div> <h3>Fecha: {el["fecha"]}</h3> <p>Nombre: {Cliente.nombre}</p> \n <p>Apellido: {Cliente.apellido}</p> <p>Numero: {Cliente.numero}</p> \n <p>Dni: {Cliente.dni}</p> \n <p> Tipo: {el["tipo"]} </p> \n <p> Estado: {el["estado"]} </p> \n <p> Monto: {el["monto"]} <p>Motivo de rechazo: El monto de retiro excede su saldo en cuenta</p>\n')
                        
                    elif el['estado'] == 'RECHAZADA' and el['tipo'] == 'ALTA_TARJETA_CREDITO':
                            agregar_registros = file.writelines(f'<div> <h3>Fecha: {el["fecha"]}</h3> <p>Nombre: {Cliente.nombre}</p> \n <p>Apellido: {Cliente.apellido}</p> <p>Numero: {Cliente.numero}</p> \n <p>Dni: {Cliente.dni}</p> \n <p> Tipo: {el["tipo"]} </p> \n <p> Estado: {el["estado"]} </p> \n <p> Monto: {el["monto"]} <p>Motivo de rechazo: El limite de 1 tarjeta de credito ya fue alcanzado\n')
                        
                    elif el['estado'] == 'RECHAZADA' and el['tipo'] == 'ALTA_CHEQUERA':
                            agregar_registros = file.writelines(f'<div> <h3>Fecha: {el["fecha"]}</h3> <p>Nombre: {Cliente.nombre}</p> \n <p>Apellido: {Cliente.apellido}</p> <p>Numero: {Cliente.numero}</p> \n <p>Dni: {Cliente.dni}</p> \n <p> Tipo: {el["tipo"]} </p> \n <p> Estado: {el["estado"]} </p> \n <p> Monto: {el["monto"]} <p>Motivo de rechazo: El limite de 1 chequera ya fue alcanzado\n')

                    elif el['estado'] == 'RECHAZADA' and el['tipo'] == 'COMPRA_DOLAR':
                            agregar_registros = file.writelines(f'<div> <h3>Fecha: {el["fecha"]}</h3> <p>Nombre: {Cliente.nombre}</p> \n <p>Apellido: {Cliente.apellido}</p> <p>Numero: {Cliente.numero}</p> \n <p>Dni: {Cliente.dni}</p> \n <p> Tipo: {el["tipo"]} </p> \n <p> Estado: {el["estado"]} </p> \n <p> Monto: {el["monto"]} <p>Motivo de rechazo: Saldo insuficiente para hacer la conversion\n' )

                    elif el['estado'] == 'RECHAZADA' and el['tipo'] == 'TRANSFERENCIA_ENVIADA':
                        if el['monto'] > el['cupoDiarioRestante']:
                            agregar_registros = file.writelines(
                                f'<div> <h3>Fecha: {el["fecha"]}</h3> <p>Nombre: {Cliente.nombre}</p> \n <p>Apellido: {Cliente.apellido}</p> <p>Numero: {Cliente.numero}</p> \n <p>Dni: {Cliente.dni}</p> \n <p> Tipo: {el["tipo"]} </p> \n <p> Estado: {el["estado"]} </p> \n <p> Monto: {el["monto"]} </p> \n <p>Motivo de rechazo: Excedio el limite diario \n </div>')
                        elif el['monto'] > el['saldoEnCuenta']:
                            agregar_registros = file.writelines(
                                f'<div> <h3>Fecha: {el["fecha"]}</h3> <p>Nombre: {Cliente.nombre}</p> \n <p>Apellido: {Cliente.apellido}</p> <p>Numero: {Cliente.numero}</p> \n <p>Dni: {Cliente.dni}</p> \n <p> Tipo: {el["tipo"]} </p> \n <p> Estado: {el["estado"]} </p> \n <p> Monto: {el["monto"]} </p> \n <p>Motivo de rechazo: Saldo insuficiente para realizar la transferencia\n </div>')
                    elif el['estado'] == 'RECHAZADA' and el['tipo'] == 'TRANSFERENCIA_RECIBIDA': agregar_registros = file.writelines(f'<div> <h3>Fecha: {el["fecha"]}</h3> <p>Nombre: {Cliente.nombre}</p> \n <p>Apellido: {Cliente.apellido}</p> <p>Numero: {Cliente.numero}</p> \n <p>Dni: {Cliente.dni}</p> \n <p> Tipo: {el["tipo"]} </p> \n <p> Estado: {el["estado"]} </p> \n <p> Monto: {el["monto"]}<p>Motivo de rechazo: La transferencia no fue autorizada \n')

    clienteGold = Gold(datos_del_cliente['nombre'], datos_del_cliente['apellido'], datos_del_cliente['numero'], datos_del_cliente['dni'], datos_del_cliente['tipo'])

    print(clienteGold.verificaciones())
if cliente1.tipo == 'BLACK':
    
    class Black (Cliente):
        def __init__(Cliente, nombre, apellido, numero, dni, tipo):
            super().__init__(nombre, apellido, numero, dni, tipo)

        def puede_crear_chequera(Clientes):
            return True

        def puede_crear_tarjeta_credito(Clientes):
            return True
        
        def puede_comprar_dolar(Clientes):
            return True

        def verificaciones(Clientes):
            with open('transacciones.html', 'a') as file:
                agregar_registros = file.write(f'css')                  

            for el in datos_del_cliente['transacciones']:
                with open('transacciones.html', 'a') as file:  
                    if el['estado'] == 'ACEPTADA':
                        agregar_registros = file.writelines(f'<div> <h3>Fecha: {el["fecha"]}</h3> <p>Nombre: {Cliente.nombre}</p> \n <p>Apellido: {Cliente.apellido}</p> <p>Numero: {Cliente.numero}</p> \n <p>Dni: {Cliente.dni}</p> \n <p> Tipo: {el["tipo"]} </p> \n <p> Estado: {el["estado"]} </p> \n <p> Monto: {el["monto"]}')

                    if el['estado'] == 'RECHAZADA' and el['tipo'] == 'RETIRO_EFECTIVO_CAJERO_AUTOMATICO':
                        if el['cupoDiarioRestante'] < el['monto']:
                            agregar_registros = file.writelines(f'<div> <h3>Fecha: {el["fecha"]}</h3> <p>Nombre: {Cliente.nombre}</p> \n <p>Apellido: {Cliente.apellido}</p> <p>Numero: {Cliente.numero}</p> \n <p>Dni: {Cliente.dni}</p> \n <p> Tipo: {el["tipo"]} </p> \n <p> Estado: {el["estado"]} </p> \n <p> Monto: {el["monto"]} <p>Motivo de rechazo: El monto de retiro excede su saldo disponible diario</p>\n')
                        elif el['monto'] > el['saldoEnCuenta']:
                            agregar_registros = file.writelines(f'<div> <h3>Fecha: {el["fecha"]}</h3> <p>Nombre: {Cliente.nombre}</p> \n <p>Apellido: {Cliente.apellido}</p> <p>Numero: {Cliente.numero}</p> \n <p>Dni: {Cliente.dni}</p> \n <p> Tipo: {el["tipo"]} </p> \n <p> Estado: {el["estado"]} </p> \n <p> Monto: {el["monto"]} <p>Motivo de rechazo: El monto de retiro es mayor al saldo en cuenta</p>\n')

                    elif el['estado'] == 'RECHAZADA' and el['tipo'] == 'ALTA_TARJETA_CREDITO':
                            agregar_registros = file.writelines(f'<div> <h3>Fecha: {el["fecha"]}</h3> <p>Nombre: {Cliente.nombre}</p> \n <p>Apellido: {Cliente.apellido}</p> <p>Numero: {Cliente.numero}</p> \n <p>Dni: {Cliente.dni}</p> \n <p> Tipo: {el["tipo"]} </p> \n <p> Estado: {el["estado"]} </p> \n <p> Monto: {el["monto"]} <p>Motivo de rechazo: El limite de 5 tarjetas de credito ya fue alcanzado\n')
                        
                    elif el['estado'] == 'RECHAZADA' and el['tipo'] == 'ALTA_CHEQUERA':
                            agregar_registros = file.writelines(f'<div> <h3>Fecha: {el["fecha"]}</h3> <p>Nombre: {Cliente.nombre}</p> \n <p>Apellido: {Cliente.apellido}</p> <p>Numero: {Cliente.numero}</p> \n <p>Dni: {Cliente.dni}</p> \n <p> Tipo: {el["tipo"]} </p> \n <p> Estado: {el["estado"]} </p> \n <p> Monto: {el["monto"]} <p>Motivo de rechazo: El limite de 2 chequeras ya fue alcanzado\n')

                    elif el['estado'] == 'RECHAZADA' and el['tipo'] == 'COMPRA_DOLAR':
                            agregar_registros = file.writelines(f'<div> <h3>Fecha: {el["fecha"]}</h3> <p>Nombre: {Cliente.nombre}</p> \n <p>Apellido: {Cliente.apellido}</p> <p>Numero: {Cliente.numero}</p> \n <p>Dni: {Cliente.dni}</p> \n <p> Tipo: {el["tipo"]} </p> \n <p> Estado: {el["estado"]} </p> \n <p> Monto: {el["monto"]} <p>Motivo de rechazo: Saldo insuficiente para hacer la conversion\n' )

                    elif el['estado'] == 'RECHAZADA' and el['tipo'] == 'TRANSFERENCIA_ENVIADA':
                            agregar_registros = file.writelines(
                                f'<div> <h3>Fecha: {el["fecha"]}</h3> <p>Nombre: {Cliente.nombre}</p> \n <p>Apellido: {Cliente.apellido}</p> <p>Numero: {Cliente.numero}</p> \n <p>Dni: {Cliente.dni}</p> \n <p> Tipo: {el["tipo"]} </p> \n <p> Estado: {el["estado"]} </p> \n <p> Monto: {el["monto"]} </p> \n <p>Motivo de rechazo: Saldo insuficiente para realizar la transferencia\n </div>')

                    elif el['estado'] == 'RECHAZADA' and el['tipo'] == 'TRANSFERENCIA_RECIBIDA':
                            agregar_registros = file.writelines(f'<div> <h3>Fecha: {el["fecha"]}</h3> <p>Nombre: {Cliente.nombre}</p> \n <p>Apellido: {Cliente.apellido}</p> <p>Numero: {Cliente.numero}</p> \n <p>Dni: {Cliente.dni}</p> \n <p> Tipo: {el["tipo"]} </p> \n <p> Estado: {el["estado"]} </p> \n <p> Monto: {el["monto"]}<p>Motivo de rechazo: Error\n')
    
    clienteBlack = Black(datos_del_cliente['nombre'], datos_del_cliente['apellido'], datos_del_cliente['numero'], datos_del_cliente['dni'], datos_del_cliente['tipo'])

    print(clienteBlack.verificaciones())


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

