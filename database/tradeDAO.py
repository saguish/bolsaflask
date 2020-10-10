from database.connection import ConnectionFactory
import json
"""
realiza 	
"""
def insert(trade_obj):
	connection = ConnectionFactory.getConnection()
	cursor = connection.cursor()


	sql_string = """
	INSERT INTO trades_table 
	(nota_liq, tipo_op, data, ativo, modalidade, mercado, qtd, preco_unit, corretagem, iss, emolumentos, liquidacao, irrf, corretora)
	values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
	"""

	# sql_parms = tuple(trade_obj.getValues())
	t = trade_obj.__dict__
	sql_parms = (t['nota_liq'],t['tipo_op'],t['data'],t['ativo'],t['modalidade'],t['mercado'],t['qtd'],t['preco_unit'],t['corretagem'],t['iss'],t['emolumentos'],t['liquidacao'],t['irrf'],t['corretora'])

	cursor.execute(sql_string,sql_parms)
	connection.commit()


def read_all():
	connection = ConnectionFactory.getConnection()
	cursor = connection.cursor()


	sql_string = """ SELECT * FROM TRADES_TABLE"""
	cursor.execute(sql_string)
	dados = cursor.fetchall()

	lista_json = []
	for d in dados:
		dado_json = {'nota_liq': d[1], 'tipo_op': d[2],'data': d[3],'ativo':d[4],'modalidade':d[5],'mercado':d[6],'qtd':d[7],
		'preco_unit':d[8],'corretagem':d[9],'iss':d[10],'emolumentos':d[11],'liquidacao':d[12],'irrf':d[13],'corretora':d[14]}

		lista_json.append(dado_json)

	return json.dumps(lista_json,indent=4, sort_keys=True, default=str)
