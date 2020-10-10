from connection import ConnectionFactory
"""função para criação automatizada da tabela trades_table"""
def setup():
	connection = ConnectionFactory.getConnection()
	cursor = connection.cursor()

	
	cmd = """CREATE TABLE IF NOT EXISTS trades_table (
   		id serial PRIMARY KEY,
		nota_liq varchar(15),
   		tipo_op varchar(6),
   		data DATE,
  		ativo varchar(8),
   		modalidade varchar(15),
		mercado varchar(10),
		qtd integer,
		preco_unit money,
		corretagem money,
		iss money,
		emolumentos money,
		liquidacao money,
		irrf money,
		corretora varchar(10)			
				);
	"""
	cursor.execute(cmd)
	connection.commit()
	print("tabela criada com sucesso")

if __name__ == "__main__":
    setup()
