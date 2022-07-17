
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
            agregar_registros = file.writelines(f'<!DOCTYPE html> \n <html lang="es"> \n <head> \n <meta charset="UTF-8"> \n <meta http-equiv="X-UA-Compatible" content="IE=edge"> \n <meta name="viewport" content="width=device-width, initial-scale=1.0">  <title>Comprobante \n </title> \n <link rel="stylesheet" href="transacciones.css"> \n <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0-beta1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-0evHe/X+R7YkIZDRvuzKMRqM+OrBnVFBL6DOitfPri4tjfHxaWutUpFmBp4vmVor" crossorigin="anonymous"> \n <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0-beta1/dist/js/bootstrap.bundle.min.js" integrity="sha384-pprn3073KE6tl6bjs2QrFaJGz5/SUsLqktiwsUTF55Jfv3qYSDhgCecCxMW52nD2" crossorigin="anonymous">  </script> \n </head>')
            agregar_registros = file.writelines(f'\n <body> \n <h1 class="titulo">Ultimos movimientos de cuenta</h1> \n <div class="card" style="width: 18rem;"> \n <div class="card-header">')
            agregar_registros = file.writelines(f'{self.nombre} {self.apellido} - {self.tipo} \n </div> \n <ul class="list-group list-group-flush"> \n <li class="list-group-item">')
            agregar_registros = file.writelines(f'Nro de Cuenta:  {self.numero} </li> \n <li class="list-group-item"> DNI:  {self.dni} </li> \n <li class="list-group-item"> Direccion: {self.direccion}</li> \n </ul> \n </div> \n </div>')
            agregar_registros = file.writelines(f'<table class="table">')
            agregar_registros = file.writelines(f'<thead> \n <tr class="filas"> \n <th scope="col">Fecha</th> \n <th scope="col">Tipo</th> \n <th scope="col">Estado</th> \n <th scope="col">Monto</th> \n <th scope="col">Motivo de rechazo</th> \n </tr> \n </thead> \n <tbody>')  
            for el in abriendo_json.datos_del_cliente['transacciones']:
                    if el['estado'] == 'ACEPTADA':
                        agregar_registros = file.writelines(f'<tr class="aceptada1"> \n <th scope="row"> {el["fecha"]}</td>  \n <td> {el["tipo"]}</td> \n <td class="estado">{el["estado"]} </td> \n <td> : {el["monto"]} </td> \n <td>-</td> </tr>')
                    
                    if el['estado'] == 'RECHAZADA' and el['tipo'] == 'RETIRO_EFECTIVO_CAJERO_AUTOMATICO':
                        if el['cupoDiarioRestante'] < el['monto']:
                            agregar_registros = file.writelines(f'<tr class="rechazada1"> \n <th scope="row"> {el["fecha"]}</td>  \n <td> {el["tipo"]}</td> \n <td class="estado">{el["estado"]} </td> \n <td> : {el["monto"]} </td> \n <td> El monto de retiro excede su saldo disponible diario</p>\n')
                        elif el['monto'] > el['saldoEnCuenta']:
                            agregar_registros = file.writelines(f'<tr class="rechazada1"> \n <th scope="row"> {el["fecha"]}</td>  \n <td> {el["tipo"]}</td> \n <td class="estado">{el["estado"]} </td> \n <td> : {el["monto"]} </td> \n <td> El monto de retiro excede su saldo en cuenta</p>\n')
                        
                    elif el['estado'] == 'RECHAZADA' and el['tipo'] == 'ALTA_TARJETA_CREDITO':
                            agregar_registros = file.writelines(f'<tr class="rechazada1"> \n <th scope="row"> {el["fecha"]}</td>  \n <td> {el["tipo"]}</td> \n <td class="estado">{el["estado"]} </td> \n <td> : {el["monto"]} </td> \n <td> Usted no puede solicitar una tarjeta de credito\n')
                        
                    elif el['estado'] == 'RECHAZADA' and el['tipo'] == 'ALTA_CHEQUERA':
                            agregar_registros = file.writelines(f'<tr class="rechazada1"> \n <th scope="row"> {el["fecha"]}</td>  \n <td> {el["tipo"]}</td> \n <td class="estado">{el["estado"]} </td> \n <td> : {el["monto"]} </td> \n <td> Usted no puede solicitar una chequera\n')

                    elif el['estado'] == 'RECHAZADA' and el['tipo'] == 'COMPRA_DOLAR':
                            agregar_registros = file.writelines(f'<tr class="rechazada1"> \n <th scope="row"> {el["fecha"]}</td>  \n <td> {el["tipo"]}</td> \n <td class="estado">{el["estado"]} </td> \n <td> : {el["monto"]} </td> \n <td> Usted no puede comprar dólares\n' )

                    elif el['estado'] == 'RECHAZADA' and el['tipo'] == 'TRANSFERENCIA_ENVIADA':
                        if el['monto'] == el['saldoEnCuenta'] or el['monto'] > el['saldoEnCuenta']:
                            agregar_registros = file.writelines(f'<tr class="rechazada1"> \n <th scope="row"> {el["fecha"]}</td>  \n <td> {el["tipo"]}</td> \n <td class="estado">{el["estado"]} </td> \n <td> : {el["monto"]} </td> \n <td> Saldo insuficiente para realizar la transferencia. Acuerdense que se le suma el {cuenta.costo_transferencias}% del monto de la transferencia.\n </div>')

                    elif el['estado'] == 'RECHAZADA' and el['tipo'] == 'TRANSFERENCIA_RECIBIDA': 
                        if el['monto'] > cuenta.limite_transferencia_recibida:
                            agregar_registros = file.writelines(f'<tr class="rechazada1"> \n <th scope="row"> {el["fecha"]}</td>  \n <td> {el["tipo"]}</td> \n <td class="estado">{el["estado"]} </td> \n <td> : {el["monto"]} </td> \n <td> No puede recibir transferencias mayores a {cuenta.limite_transferencia_recibida}\n')



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
            agregar_registros = file.writelines(f'<!DOCTYPE html> \n <html lang="es"> \n <head> \n <meta charset="UTF-8"> \n <meta http-equiv="X-UA-Compatible" content="IE=edge"> \n <meta name="viewport" content="width=device-width, initial-scale=1.0">  <title>Comprobante \n </title> \n <link rel="stylesheet" href="transacciones.css"> \n <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0-beta1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-0evHe/X+R7YkIZDRvuzKMRqM+OrBnVFBL6DOitfPri4tjfHxaWutUpFmBp4vmVor" crossorigin="anonymous"> \n <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0-beta1/dist/js/bootstrap.bundle.min.js" integrity="sha384-pprn3073KE6tl6bjs2QrFaJGz5/SUsLqktiwsUTF55Jfv3qYSDhgCecCxMW52nD2" crossorigin="anonymous">  </script> \n </head>')
            agregar_registros = file.writelines(f'\n <body> \n <h1 class="titulo">Ultimos movimientos de cuenta</h1> \n <div class="card" style="width: 18rem;"> \n <div class="card-header">')
            agregar_registros = file.writelines(f'{self.nombre} {self.apellido} - {self.tipo} \n </div> \n <ul class="list-group list-group-flush"> \n <li class="list-group-item">')
            agregar_registros = file.writelines(f'Nro de Cuenta:  {self.numero} </li> \n <li class="list-group-item"> DNI:  {self.dni} </li> \n <li class="list-group-item"> Direccion: {self.direccion}</li> \n </ul> \n </div> \n </div>')
            agregar_registros = file.writelines(f'<table class="table">')
            agregar_registros = file.writelines(f'<thead> \n <tr class="filas"> \n <th scope="col">Fecha</th> \n <th scope="col">Tipo</th> \n <th scope="col">Estado</th> \n <th scope="col">Monto</th> \n <th scope="col">Motivo de rechazo</th> \n </tr> \n </thead> \n <tbody>')  
            for el in abriendo_json.datos_del_cliente['transacciones']:
                    if el['estado'] == 'ACEPTADA':
                        agregar_registros = file.writelines(f'<tr class="aceptada1"> \n <th scope="row"> {el["fecha"]}</td>  \n <td> {el["tipo"]}</td> \n <td class="estado">{el["estado"]} </td> \n <td> : {el["monto"]} </td> \n <td>-</td> </tr>')

                    if el['estado'] == 'RECHAZADA' and el['tipo'] == 'RETIRO_EFECTIVO_CAJERO_AUTOMATICO':
                        if el['cupoDiarioRestante'] < el['monto']:
                            agregar_registros = file.writelines(f'<tr class="rechazada1"> \n <th scope="row"> {el["fecha"]}</td>  \n <td> {el["tipo"]}</td> \n <td class="estado">{el["estado"]} </td> \n <td> : {el["monto"]} </td> \n <td> El monto de retiro excede su saldo disponible diario</p>\n')
                        elif el['monto'] > el['saldoEnCuenta']:
                            agregar_registros = file.writelines(f'<tr class="rechazada1"> \n <th scope="row"> {el["fecha"]}</td>  \n <td> {el["tipo"]}</td> \n <td class="estado">{el["estado"]} </td> \n <td> : {el["monto"]} </td> \n <td> El monto de retiro excede su saldo en cuenta</p>\n')
                        
                    elif el['estado'] == 'RECHAZADA' and el['tipo'] == 'ALTA_TARJETA_CREDITO':
                        if Gold.puede_crear_tarjeta_credito() == el['totalTarjetasDeCreditoActualmente']:
                            agregar_registros = file.writelines(f'<tr class="rechazada1"> \n <th scope="row"> {el["fecha"]}</td>  \n <td> {el["tipo"]}</td> \n <td class="estado">{el["estado"]} </td> \n <td> : {el["monto"]} </td> \n <td> El limite de 1 tarjeta de credito ya fue alcanzado\n')
                        
                    elif el['estado'] == 'RECHAZADA' and el['tipo'] == 'ALTA_CHEQUERA':
                        if Gold.puede_crear_chequera() == el['totalChequerasActualmente']:
                            agregar_registros = file.writelines(f'<tr class="rechazada1"> \n <th scope="row"> {el["fecha"]}</td>  \n <td> {el["tipo"]}</td> \n <td class="estado">{el["estado"]} </td> \n <td> : {el["monto"]} </td> \n <td> El limite de 1 chequera ya fue alcanzado\n')

                    elif el['estado'] == 'RECHAZADA' and el['tipo'] == 'COMPRA_DOLAR':
                            agregar_registros = file.writelines(f'<tr class="rechazada1"> \n <th scope="row"> {el["fecha"]}</td>  \n <td> {el["tipo"]}</td> \n <td class="estado">{el["estado"]} </td> \n <td> : {el["monto"]} </td> \n <td> Saldo insuficiente para hacer la compra\n' )

                    elif el['estado'] == 'RECHAZADA' and el['tipo'] == 'TRANSFERENCIA_ENVIADA':
                        if el['monto'] > el['saldoEnCuenta'] or el['monto'] == el['saldoEnCuenta']:
                            agregar_registros = file.writelines(f'<tr class="rechazada1"> \n <th scope="row"> {el["fecha"]}</td>  \n <td> {el["tipo"]}</td> \n <td class="estado">{el["estado"]} </td> \n <td> : {el["monto"]} </td> \n <td> Saldo insuficiente para realizar la transferencia. Acuerdense que se le suma el {cuenta.costo_transferencias}% del monto de la transferencia\n </div>')
                    
                    elif el['estado'] == 'RECHAZADA' and el['tipo'] == 'TRANSFERENCIA_RECIBIDA': 
                        if cuenta.limite_transferencia_recibida < el['monto']:
                            agregar_registros = file.writelines(f'<tr class="rechazada1"> \n <th scope="row"> {el["fecha"]}</td>  \n <td> {el["tipo"]}</td> \n <td class="estado">{el["estado"]} </td> \n <td> : {el["monto"]} </td> \n <td> La transferencia es mayor a lo permitido, {cuenta.limite_transferencia_recibida}</td> \n </tr> \n')

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
            agregar_registros = file.writelines(f'<!DOCTYPE html> \n <html lang="es"> \n <head> \n <meta charset="UTF-8"> \n <meta http-equiv="X-UA-Compatible" content="IE=edge"> \n <meta name="viewport" content="width=device-width, initial-scale=1.0">  <title>Comprobante \n </title> \n <link rel="stylesheet" href="transacciones.css"> \n <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0-beta1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-0evHe/X+R7YkIZDRvuzKMRqM+OrBnVFBL6DOitfPri4tjfHxaWutUpFmBp4vmVor" crossorigin="anonymous"> \n <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0-beta1/dist/js/bootstrap.bundle.min.js" integrity="sha384-pprn3073KE6tl6bjs2QrFaJGz5/SUsLqktiwsUTF55Jfv3qYSDhgCecCxMW52nD2" crossorigin="anonymous">  </script> \n </head>')
            agregar_registros = file.writelines(f'\n <body> \n <h1 class="titulo">Ultimos movimientos de cuenta</h1> \n <div class="card" style="width: 18rem;"> \n <div class="card-header">')
            agregar_registros = file.writelines(f'{self.nombre} {self.apellido} - {self.tipo} \n </div> \n <ul class="list-group list-group-flush"> \n <li class="list-group-item">')
            agregar_registros = file.writelines(f'Nro de Cuenta:  {self.numero} </li> \n <li class="list-group-item"> DNI:  {self.dni} </li> \n <li class="list-group-item"> Direccion: {self.direccion}</li> \n </ul> \n </div> \n </div>')
            agregar_registros = file.writelines(f'<table class="table">')
            agregar_registros = file.writelines(f'<thead> \n <tr class="filas"> \n <th scope="col">Fecha</th> \n <th scope="col">Tipo</th> \n <th scope="col">Estado</th> \n <th scope="col">Monto</th> \n <th scope="col">Motivo de rechazo</th> \n </tr> \n </thead> \n <tbody>')
            for el in abriendo_json.datos_del_cliente['transacciones']:
                    if el['estado'] == 'ACEPTADA':#link href= st
                        agregar_registros = file.writelines(f'<tr class="aceptada1"> \n <th scope="row"> {el["fecha"]}</td>  \n <td> {el["tipo"]}</td> \n <td class="estado">{el["estado"]} </td> \n <td> : {el["monto"]} </td> \n <td>-</td> </tr>')

                    if el['estado'] == 'RECHAZADA' and el['tipo'] == 'RETIRO_EFECTIVO_CAJERO_AUTOMATICO':
                        if el['cupoDiarioRestante'] < el['monto']:
                            agregar_registros = file.writelines(f'<tr class="rechazada1"> \n <th scope="row"> {el["fecha"]}</td>  \n <td> {el["tipo"]}</td> \n <td class="estado">{el["estado"]} </td> \n <td> : {el["monto"]} </td> \n <td> El monto de retiro excede su saldo disponible diario</td>\n </tr>')
                        elif el['monto'] > el['saldoEnCuenta']:
                            agregar_registros = file.writelines(f'<tr class="rechazada1"> \n <th scope="row"> {el["fecha"]}</td>  \n <td> {el["tipo"]}</td> \n <td class="estado">{el["estado"]} </td> \n <td> : {el["monto"]} </td> \n <td> El monto de retiro es mayor al saldo en cuenta</td>\n </tr>')

                    elif el['estado'] == 'RECHAZADA' and el['tipo'] == 'ALTA_TARJETA_CREDITO':
                        if Black.puede_crear_tarjeta_credito() == el['totalTarjetasDeCreditoActualmente']:
                            agregar_registros = file.writelines(f'<tr class="rechazada1"> \n <th scope="row"> {el["fecha"]}</td>  \n <td> {el["tipo"]}</td> \n <td class="estado">{el["estado"]} </td> \n <td> : {el["monto"]} </td> \n <td> El limite de 5 tarjetas de credito ya fue alcanzado</td> \n </tr>')
                        
                    elif el['estado'] == 'RECHAZADA' and el['tipo'] == 'ALTA_CHEQUERA':
                        if Black.puede_crear_chequera() == el['totalChequerasActualmente']:
                            agregar_registros = file.writelines(f'<tr class="rechazada1"> \n <th scope="row"> {el["fecha"]}</td>  \n <td> {el["tipo"]}</td> \n <td class="estado">{el["estado"]} </td> \n <td> : {el["monto"]} </td> \n <td> El limite de 2 chequeras ya fue alcanzado</td> \n </tr>')

                    elif el['estado'] == 'RECHAZADA' and el['tipo'] == 'COMPRA_DOLAR':
                            agregar_registros = file.writelines(f'<tr class="rechazada1"> \n <th scope="row"> {el["fecha"]}</td>  \n <td> {el["tipo"]}</td> \n <td class="estado">{el["estado"]} </td> \n <td> : {el["monto"]} </td> \n <td> Saldo insuficiente para hacer la conversion</td> \n </tr>' )

                    elif el['estado'] == 'RECHAZADA' and el['tipo'] == 'TRANSFERENCIA_ENVIADA':
                            agregar_registros = file.writelines(f'<tr class="rechazada1"> \n <th scope="row"> {el["fecha"]}</td>  \n <td> {el["tipo"]}</td> \n <td class="estado">{el["estado"]} </td> \n <td> : {el["monto"]} </td> \n <td> Saldo insuficiente para realizar la transferencia</td> \n </tr>')
            agregar_registros = file.writelines(f'</tr> \n </tbody> \n </table> \n </body> \n </html>')        
