from connection import ConnectionFactory

def setup():
	connection = ConnectionFactory.getConnection()
	cursor = connection.cursor()
	# CREATE TABLE
	
	cmd = """CREATE TABLE IF NOT EXISTS scan_table (
   		filename varchar(300),
   		dir_path varchar(500),
   		full_path varchar(500),
  		hash varchar(500),
   		device_id varchar(200)
				);
	"""
	cursor.execute(cmd)
	connection.commit()
	print("tabela criada com sucesso")

if __name__ == "__main__":
    setup()