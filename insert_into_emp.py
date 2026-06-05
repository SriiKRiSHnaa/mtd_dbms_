import pymysql
import db_connect2 as dbc2

def insert_into_employee():
    query = 'insert into emp(name, age, salary, phone) values(%s, %s, %s, %s)'
    try:
        connection = dbc2.db_connect()
        cursor = connection.cursor()
        name = input('Enter name: ')
        age = int(input('Enter age: '))
        salary = float(input('Enter salary: '))
        phone = int(input('Enter phone: ')) 
        values = (name, age, salary, phone)
        result = cursor.execute(query, values)
        connection.commit()
        cursor.close()
        dbc2.db_disconnect(connection)
        if result == 1:
            print('Record inserted')
        else:
            print('Record insertion failed')
    except Exception as e:
        print('Record insertion failed', e)

insert_into_employee()