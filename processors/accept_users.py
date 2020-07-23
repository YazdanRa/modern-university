from texttable import Texttable

from models import User


def set_role(user):
    print(Texttable().add_rows([
        ['#', 'role'],
        ['A', 'Admin'],
        ['T', 'Teacher'],
        ['S', 'Student'],
    ]).draw())
    role = input("""
        
    Now Enter the tole of the user you wanna active they!
    Enter C for cancel the process and back to the menu
    
    """).lower()
    if role == 'a':
        user.is_admin = True
        user.is_active = True
        user.save()
        print('Admin successfully activated!')
    elif role == 't':
        user.is_teacher = True
        user.is_active = True
        user.save()
        print('Teacher successfully activated!')
    elif role == 's':
        user.is_student = True
        user.is_active = True
        user.save()
        print('Student successfully activated!')
    elif role == 'c':
        print('The process has been canceled!')
    else:
        print('Enter a valid letter!')
        return False
    return True


def setup():
    users = User.select().where(User.is_active == False)
    table = Texttable()
    table.add_row(['ID', 'Student Number'])
    for user in users:
        table.add_row([user.id, user.student_number])
    print(table.draw())
    print("""
    
    Now send the ID of target you want to active it!
    although send 0 to cancel the process and back to menu
    
    """)
    try:
        id = int(input())
        if id == 0:
            print('The process has been canceled!')
            return True
        user = User.get(User.id == id)
        if user:
            while not set_role(user):
                pass
        else:
            print('You should enter a valid number!')
            return False
    except:
        print('You should enter a number!')
        return False
