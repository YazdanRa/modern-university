def setup(user):
    user.first_name = input('Enter your first name: ')
    user.last_name = input('Enter your last name: ')
    user.save()
    print('your information successfully updated!')
