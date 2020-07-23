def setup(user):
    user.first_name = input('Enter your first name: ')
    user.last_name = input('Enter your last name: ')
    user.hometown = input('Enter your hometown: ')
    user.national_id = input('Enter your National ID: ')
    user.save()
    print('your information successfully updated!')
