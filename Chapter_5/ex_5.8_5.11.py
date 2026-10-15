# ex.5.8
# user_names = ['denis', 'alex', 'admin', 'sergei', 'ivan']
# for user_name in user_names:
#     if user_name != 'admin':
#         print(f'Hello {user_name.title()}, thank you for loggin in.')
#     elif user_name == 'admin':
#         print(f'Hello {user_name}, would you like to take at status report?')
# print()

# ex.5.9
# user_names = []
# if user_names:
#     for user_name in user_names:
#         if user_name != 'admin':
#             print(f'Hello {user_name.title()}, thank you for loggin in.')
#         elif user_name == 'admin':
#             print(f'Hello {user_name}, would you like to take at status report?')
# else:
#     print('User name list is empety')

# ex.5.10
current_users = ['Denis', 'Alex', 'admin', 'Sergei', 'Ivan', 'Jhon']
current_users_low = []
for current_user in current_users:
    current_users_low.append(current_user.lower())
new_users = ['valentin', 'alex', 'semen', 'sergei', 'grisha', 'JHON']
for new_user in new_users:
    if new_user.lower() in current_users_low:
        print(f'Username {new_user.title()} already exists.')
    if new_user.lower() not in current_users_low:
        print(f'Username {new_user.title()} is available.')

# ex.5.11
number_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
for number in number_list:
    if number == '1':
        print(number + 'st')
    elif number == '2':
        print(number + 'nd')
    elif number == '3':
        print(number + 'rd')
    else:
        print(number + 'th')