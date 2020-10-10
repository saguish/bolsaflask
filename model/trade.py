import json
import datetime

class Trade(object):
	"""docstring for Trade
	clase para modelar uma transação de compra ou venda de ativo"""

	def __init__(self, json_obj):
		
		obj = json.loads(json_obj)

		self.nota_liq = obj['nota_liq']
		self.tipo_op = obj['tipo_op']
		self.data = datetime.datetime.strptime(obj['data'],'%d/%m/%Y')
		self.ativo = obj['ativo']
		self.modalidade = obj['modalidade']
		self.mercado = obj['mercado']
		self.qtd = obj['qtd']
		self.preco_unit = obj['preco_unit']
		self.corretagem = obj['corretagem']
		self.iss = obj['iss']
		self.emolumentos = obj['emolumentos']
		self.liquidacao = obj['liquidacao']
		self.irrf = obj['irrf']
		self.corretora = obj['corretora']

	def getValues(self):
		return self.__dict__.values()

