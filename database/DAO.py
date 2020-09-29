def insert(connection, filename, dir_path, full_path, hashed, device_id):
	cursor = connection.cursor()
	sql_string = """INSERT INTO scan_table (filename,dir_path,full_path,hash,device_id) values (%s,%s,%s,%s,%s)"""
	sql_parms = (filename, dir_path, full_path, hashed, device_id)
	cursor.execute(sql_string,sql_parms)
	connection.commit()
