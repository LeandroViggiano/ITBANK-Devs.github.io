
import abriendo_json

#--------------------------------
import cliente_y_cuenta

cliente_y_cuenta.cliente1 = cliente_y_cuenta.Cliente(abriendo_json.datos_del_cliente['nombre'], abriendo_json.datos_del_cliente['apellido'], abriendo_json.datos_del_cliente['numero'], abriendo_json.datos_del_cliente['dni'], abriendo_json.datos_del_cliente['tipo'])


import cliente_y_cuenta
if cliente_y_cuenta.cliente1.tipo == 'CLASSIC':
    cuenta = cliente_y_cuenta.Cuenta(10000, 150000, 0.1, 0)
elif cliente_y_cuenta.cliente1.tipo == 'GOLD':
    cuenta = cliente_y_cuenta.Cuenta(20000, 500000, 0.05, 10000)
elif cliente_y_cuenta.cliente1.tipo== 'BLACK':
    cuenta = cliente_y_cuenta.Cuenta(100000, 0, 0, 10000)



class Classic (cliente_y_cuenta.Cliente):
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
        with open('transacciones.html', 'w') as file:  
            for el in abriendo_json.datos_del_cliente['transacciones']:
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
    print("Importacion Classic correcta")


class Gold (cliente_y_cuenta.Cliente):
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
        with open('transacciones.html', 'w') as file:  
            for el in abriendo_json.datos_del_cliente['transacciones']:
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
    print("Importacion Gold correcta")



class Black (cliente_y_cuenta.Cliente):
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
        with open('transacciones.html', 'w') as file:  
            for el in abriendo_json.datos_del_cliente['transacciones']:
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
    print("Importacion Black correcta")


