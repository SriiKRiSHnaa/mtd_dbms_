import pymysql
import db_connect2 as dbc2

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


def create_db():
    query = 'create database if not exists krishna_db'
    try:
        connection = dbc2.db_connect()
        cursor = connection.cursor()
        result = cursor.execute(query)
        connection.commit()
        cursor.close()
        #connection.close()
        dbc2.db_disconnect(connection)
        if result == 1:
            print('DB created')
        else:
            print('DB already exist')

    except Exception as e:
        print('DB creation failed', e)

def create_table():
    query = 'create table if not exists employees(id int primary key auto_increment, name varchar(20), age int, salary float, phone bigint unique)'
    try:
        connection = dbc2.db_connect()
        cursor = connection.cursor()
        result = cursor.execute(query)
        connection.commit()
        cursor.close()
        #connection.close()
        dbc2.db_disconnect(connection)
        if result == 1:
            print('Table created')
        else:
            print('Table already exists')
    except Exception as e:
        print('Table creation failed', e)

def read_employee():
    name = input('Enter name: ')
    age = int(input('Enter age: '))
    salary = float(input('Enter salary: '))
    phone = int(input('Enter phone: ')) 
    return (name, age, salary, phone)

def insert_employee():
    query = 'insert into employees(name, age, salary, phone) values(%s, %s, %s, %s)'
    try:
        connection = dbc2.db_connect()
        cursor = connection.cursor()
        employee = read_employee()
        result = cursor.execute(query, employee)
        connection.commit()
        cursor.close()
        dbc2.db_disconnect(connection)
        if result == 1:
            print('Record inserted')
        else:
            print('Record insertion failed')
    except Exception as e:
        print('Record insertion failed', e)

def update_employee(): 
    id = int(input('Enter employee id whose salary should be updated: '))
    salary = float(input('Enter new salary: '))    
    query = 'update employees set salary=%s where id=%s'
    try:
        connection = dbc2.db_connect()
        cursor = connection.cursor()
        result = cursor.execute(query, (salary,id))
        connection.commit()
        cursor.close()
        dbc2.db_disconnect(connection)
        if result == 1:
            print('Record Updated')
        else:
            print('Record update failed')
    except Exception as e:
        print('Record update failed', e)

def delete_employee():
    id = int(input('Enter id of the employee to be deleted : '))
    query = 'delete from employees where id=%s'
    try:
        connection = dbc2.db_connect()
        cursor = connection.cursor()
        result = cursor.execute(query, id)
        connection.commit()
        cursor.close()
        dbc2.db_disconnect(connection)
        if result == 1:
            print(f'Employee with id {id} deleted')
        else:
            print(f'Employee with id {id} not found')
    except Exception as e:
        print('Employee deletion failed', e)


def search_employee():
    id = int(input('Enter employee id to search: '))    
    query = 'select * from employees where id=%s'
    try:
        connection = dbc2.db_connect()
        cursor = connection.cursor()
        cursor.execute(query, id)
        row = cursor.fetchone()
        if row:
            print(row)
        else:
            print(f'Employee with id {id} not found')
        cursor.close()
        dbc2.db_disconnect(connection)
    except Exception as e:
        print('Employee search failed', e)


def list_employees(): 
    query = 'select * from employees'
    try:
        connection = dbc2.db_connect()
        cursor = connection.cursor()
        cursor.execute(query)
        rows = cursor.fetchmany()
        if rows:
            for row in rows:
                print(row)
        else:
            print(f'No Employee Record was Found')
        cursor.close()
        dbc2.db_disconnect(connection)
    except Exception as e:
        print('Employee listing failed', e)

list_employees()