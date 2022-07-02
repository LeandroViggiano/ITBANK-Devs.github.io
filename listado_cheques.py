from datetime import datetime
import sys
import csv

# caso en el que el usuario SI especifique el estado del cheque
if len(sys.argv) == 6:

    # Asignamos un valor a cada SYS.ARGV
    nombreArchivo = sys.argv[1]
    dni = sys.argv[2]
    salida = sys.argv[3]
    tipoCheque = sys.argv[4]
    estadoCheque = sys.argv[5]

    fechaActual = datetime.now().strftime('%Y-%m-%d %H-%M-%S')
    
    
    
    if salida == 'PANTALLA':
        
        # Llamamos al archivo CSV
        with open('registros.csv') as file:
            read = csv.reader(file)

            # En este array se guardan el Nro Cheque, Nro Cuenta, DNI
            dniant=[]
            # Se guardan los registros
            registroSolo=[]
            # En esta variable se guarda los numeros de cheques
            nrocheque=''
            # En esta variable se guarda los numeros de cuenta
            nrocuenta=''

            for registro in read:

                if registro[8] == dni and registro[9] == estadoCheque and registro[10] == tipoCheque:
                    dniant.append([registro[0], registro[3], registro[8]])
                    nrocheque+=f'{registro[0]}-'
                    nrocuenta+=f'{registro[3]}-'
                    registroSolo.append(registro)
            
            # En este array se guardan los Nro Cuentas que estan dentro del array DNIANT 
            arrayNroCuenta = []
            for el in dniant:
                for nc in el:
                    arrayNroCuenta.append(nc)

            indexNroCheque = nrocheque.index("-")
            indexNroCuenta = nrocheque.index("-")
            stringNroCheque = nrocheque[0:indexNroCheque]
            stringNroCuenta = nrocheque[0:indexNroCuenta]
            
            # Hacemos un condicional para saber si hay registros duplicados
            if arrayNroCuenta.count(stringNroCheque) > 1 and arrayNroCuenta.count(stringNroCuenta) > 1 and dni:
                print("ERROR: Se encontro el Nro de Cheque, Nro de Cuenta y DNI duplicados")
            else:
                print(registroSolo)

    elif salida == 'CSV':
        # Llamamos al archivo CSV
        with open('registros.csv') as file:
            read = csv.reader(file)

            # En este array se guardan el Nro Cheque, Nro Cuenta, DNI
            dniant=[]
            # Se guardan los registros
            registroSolo=[]
            # En esta variable se guarda los numeros de cheques
            nrocheque=''
            # En esta variable se guarda los numeros de cuenta
            nrocuenta=''

            for registro in read:

                if registro[8] == dni and registro[9] == estadoCheque and registro[10] == tipoCheque:
                    dniant.append([registro[0], registro[3], registro[8]])
                    nrocheque+=f'{registro[0]}-'
                    nrocuenta+=f'{registro[3]}-'
                    registroSolo.append(registro)
            
            # En este array se guardan los Nro Cuentas que estan dentro del array DNIANT 
            arrayNroCuenta = []
            for el in dniant:
                for nc in el:
                    arrayNroCuenta.append(nc)

            indexNroCheque = nrocheque.index("-")
            indexNroCuenta = nrocheque.index("-")
            stringNroCheque = nrocheque[0:indexNroCheque]
            stringNroCuenta = nrocheque[0:indexNroCuenta]
            
            # Hacemos un condicional para saber si hay registros duplicados
            if arrayNroCuenta.count(stringNroCheque) > 1 and arrayNroCuenta.count(stringNroCuenta) > 1 and dni:
                print("ERROR: Se encontro el Nro de Cheque, Nro de Cuenta y DNI duplicados")
            else:
                with open(f'{dni} {fechaActual}.csv', 'a', newline='') as file:
                    write = csv.writer(file, delimiter=",")
                    write.writerow([f'Numero de Cuenta: {registro[3]}', f' Fecha Origen: {registro[6]}', f' Fecha Pago: {registro[7]}', f' Valor: ${registro[5]}'])
                


# caso en el que el usuario NO especifique el estado del cheque
if len(sys.argv) == 5:
    nombreArchivo = sys.argv[1]
    dni = sys.argv[2]
    salida = sys.argv[3]
    tipoCheque = sys.argv[4]
    fechaActual = datetime.now().strftime('%Y-%m-%d %H-%M-%S')

    if salida == 'PANTALLA':
        with open('registros.csv') as file:
            read = csv.reader(file)
            array=[]
            for registro in read:
                if registro[8] == dni and registro[10] == tipoCheque:
                    print(registro)
    elif salida == 'CSV':
        with open('registros.csv') as file:
            read = csv.reader(file)
            for registro in read:
                if registro[8] == dni:
                    with open(f'{dni} {fechaActual}.csv', 'a', newline='') as file:
                        write = csv.writer(file, delimiter=",")
                        write.writerow([f'Numero de Cuenta: {registro[3]}', f' Fecha Origen: {registro[6]}', f' Fecha Pago: {registro[7]}', f' Valor: ${registro[8]}'])


