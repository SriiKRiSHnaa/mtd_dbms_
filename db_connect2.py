import pymysql

def db_connect():
    connection = None
    try :
        connection = pymysql.connect(user = 'root', password = 'SriKrishn@04', port=3306, database='krishna_db', charset='utf8', host='localhost')
        print('DB connected')
    except Exception as e:
        print('DB connection failed')
    return connection
    
def db_disconnect(connection):
    try:
        connection.close()
        print('DB disconnected')
    except:
        print('DB disconnection failed')


