# ex.7.1
# cars = ['audi', 'volvo', 'pego']
# print('What kind you car would you like to rent?')
# brand_car = input('Enter the brand of car: ')
# if brand_car.lower() in cars:
#     print(f'We are have {brand_car} brand.')
# else:
#     print('We can not help any way.')

# ex.7.2
# print('How many people would you like to book a table?')
# book_table = int(input('Input number of people: '))
# if book_table <= 8:
#     print('Good. We have a table.')
# else:
#     print('Excuse me. We dont have a table.')

# ex.7.3
number = int(input('Input number: '))
div_rem_10 = number % 10
if div_rem_10 == 0:
    print('This nunber is multiple of 10.')
else:
    print('This nunber is DONT multiple of 10.')    