import cliente_y_cuenta
import classic_black_y_gold
#Abriendo el archivo json
import abriendo_json


#Acá creo un objeto cliente llamado c1 y le agrego los atributos de la lista datos_del_cliente


classic_black_y_gold.Classic

classic_black_y_gold.Gold

classic_black_y_gold.Black

if cliente_y_cuenta.cliente1.tipo == 'CLASSIC':
    tipoCliente = classic_black_y_gold.Classic(abriendo_json.datos_del_cliente['nombre'], abriendo_json.datos_del_cliente['apellido'], abriendo_json.datos_del_cliente['numero'], abriendo_json.datos_del_cliente['dni'], abriendo_json.datos_del_cliente['tipo'])
elif cliente_y_cuenta.cliente1.tipo == 'GOLD':
    tipoCliente = classic_black_y_gold.Gold(abriendo_json.datos_del_cliente['nombre'], abriendo_json.datos_del_cliente['apellido'], abriendo_json.datos_del_cliente['numero'], abriendo_json.datos_del_cliente['dni'], abriendo_json.datos_del_cliente['tipo'])
elif cliente_y_cuenta.cliente1.tipo == 'BLACK':
    tipoCliente = classic_black_y_gold.Black(abriendo_json.datos_del_cliente['nombre'], abriendo_json.datos_del_cliente['apellido'], abriendo_json.datos_del_cliente['numero'], abriendo_json.datos_del_cliente['dni'], abriendo_json.datos_del_cliente['tipo'])
print(tipoCliente.verificaciones()) 

