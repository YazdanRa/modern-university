def setup(user):
    new_password = input('Enter your new password:\n')
    user.password = new_password
    user.save()
    print('password successfully changed!')
