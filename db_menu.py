import sys
from db_operations import insert_employee, update_employee, delete_employee, search_employee, list_employees

def menu(choice):
    match choice:
        case 1:
            insert_employee()
        case 2:
            update_employee()
        case 3:
            delete_employee()
        case 4:
            search_employee()
        case 5:
            list_employees() 
        case 6: 
            sys.exit('End of Execution')
        case _:
            print('Invalid choice')

def run_employee_app():
    while True:
        print('1. Insert Employee')
        print('2. Update Employee Salary')
        print('3. Delete Employee')
        print('4. Search Employee')
        print('5. List Employees')
        print('6. Exit')
        choice = int(input('Enter your choice: '))
        if choice == 6:
            break
        menu(choice)

run_employee_app()