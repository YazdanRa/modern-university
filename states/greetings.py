from processors import login, register


def setup():
    msg = """
        L: Login
        R: Register
        E: Exit
    """
    print(msg)
    choice = input('Which one do you want: ').lower()
    if choice == 'l':
        login.setup()
    elif choice == 'r':
        register.setup()
    elif choice == 'e':
        exit(print('Good Bye :)'))
    else:
        print('Enter a valid letter!')
