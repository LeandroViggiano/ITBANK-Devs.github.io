
import abriendo_json
# datos_del_cliente['nombre']   #Así se llaman a los atributos del JSON, en este caso estoy llamando al atributo nombre


# PARTE CLIENTE DEL UML
class Cliente:
    def __init__(self, nombre, apellido, numero, dni, tipo):
        self.nombre = nombre
        self.apellido = apellido
        self.numero = numero
        self.dni = dni
        self.tipo = tipo
        self.direccion = (abriendo_json.datos_del_cliente['direccion']['calle'],abriendo_json.datos_del_cliente['direccion']['numero'],abriendo_json.datos_del_cliente['direccion']['ciudad'],abriendo_json.datos_del_cliente['direccion']['provincia'],abriendo_json.datos_del_cliente['direccion']['pais'])
        
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
    #print("Importacion Cliente correcta")
#Acá creo un objeto cliente llamado c1 y le agrego los atributos de la lista datos_del_cliente
# PARTE CUENTA DEL UML
class Cuenta:
    def __init__(self,limite_extraccion_diario, limite_transferencia_recibida, costo_transferencias, saldo_descubierto_disponible):
        self.limite_extraccion_diario = float(limite_extraccion_diario)
        self.limite_transferencia_recibida = float(limite_transferencia_recibida)
        self.costo_transferencias = float(costo_transferencias)
        self.saldo_descubierto_disponible = float(saldo_descubierto_disponible)
    #print("Importacion Cuenta correcta")

