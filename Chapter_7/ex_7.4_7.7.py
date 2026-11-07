# ex.7.4 and 7.6
# while True:
#     topping = input('Input pizza topping (q for exit):' )
#     if topping != 'q':
#         print(f'You pizza topping is {topping}.')
#     else:
#         print('Goodbye!')
#         break

# ex.7.5 and 7.6
# active = True
# while active:
#     age = input('Input you age (q for exit):')
#     try:
#         if int(age) < 3:
#             print('Your price for ticket free.')
#         elif 3 <= int(age) <= 12:
#             print('Your price for ticket 10$.')
#         elif int(age) > 12:
#             print('Your price for ticket 15$.')
#     except ValueError:
#         if age == 'q':
#             print('Goodbye!')
#             active = False
#         else:
#             print('Input correct value!')

# 7.6
# numb_pass = 7811
# attempts = 3
# print(f'Number of attempts: {attempts}')
# while attempts != 0:
#     user_pass = input('Pass **** - only numbers:')
#     try:    
#         if attempts > 1:
#             if int(numb_pass) == int(user_pass):
#                 print('You are saved us :D')
#                 attempts = 0
#             else:
#                 attempts -= 1
#                 if attempts > 1:
#                     print(f'Number of attempts: {attempts}')
#                 else:
#                     print('!!!NUMBER OF ATTEMPTS - 1!!!')
#         elif attempts == 1:
#             if int(numb_pass) == int(user_pass):
#                 print('You are saved us :D')
#                 attempts = 0
#             else:
#                 print(f'BOOM!!! You destroyed!!!')
#                 attempts -= 1          
#     except ValueError:
#             print('BOOM!!! You destroyed!!!')
#             attempts = 0

# 7.7
i = 10
k = 0
while i != 0:
    print(f'- # {k}')
    k += 1
