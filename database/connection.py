import psycopg2
import json

class ConnectionFactory(object):
  """classe para retorno de conexoes com o banco de dados"""


  def __init__(self, arg):
    super(ClassName, self).__init__()
    self.arg = arg

  @staticmethod
  def getConnection():
    # Opening JSON file 
    f = open('database/db_settings.json') 
      
    # returns JSON object as a dictionary 
    data = json.load(f) 

    connection_params = data['settings']

    try:
        connection = psycopg2.connect(user = connection_params['user'],
                                      password = connection_params['password'],
                                      host = connection_params['host'],
                                      port = connection_params['port'],
                                      database = connection_params['database'])

        return connection
       

    except (Exception, psycopg2.Error) as error :
      print ("Error while connecting to PostgreSQL", error)
    