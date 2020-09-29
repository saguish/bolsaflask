from connection import ConnectionFactory
import setup


# con = ConnectionFactory.getConnection()

# cursor = con.cursor()
#       # Print PostgreSQL Connection properties
# print ( con.get_dsn_parameters(),"\n")

#       # Print PostgreSQL version
# cursor.execute("SELECT version();")
# record = cursor.fetchone()
# print("You are connected to - ", record,"\n")

setup.setup()