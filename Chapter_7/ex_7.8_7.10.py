# ex.7.8
# sandwich_orders = ['chiken', 'eggs', 'beaf']
# finished_sandwichs = []
# print(f'sandwich orders list : {sandwich_orders}')
# print(f'finished sandwich list : {finished_sandwichs}\n')
# while sandwich_orders:
#     current_sand = sandwich_orders.pop(0)
#     finished_sandwichs.append(current_sand)
#     print(f'I made sandwich {current_sand}.')
# print()
# print(f'sandwich orders list : {sandwich_orders}')
# print('Finished sandwichs list :')
# for finished_sandwich in finished_sandwichs:
#     print(f'- {finished_sandwich} sandwich')

# ex.7.9
# sandwich_orders = ['chiken', 'pastrami','eggs', 
#                    'pastrami', 'beaf', 'pastrami']
# finished_sandwichs = []
# print(f'sandwich orders list : {sandwich_orders}')
# print('Sorry.. no more pastromi')
# while 'pastrami' in sandwich_orders:
#     sandwich_orders.remove('pastrami')
# print(f'finished sandwich list : {finished_sandwichs}\n')
# while sandwich_orders:
#     current_sand = sandwich_orders.pop(0)
#     finished_sandwichs.append(current_sand)
#     print(f'I made sandwich {current_sand}.')
# print()
# print(f'sandwich orders list : {sandwich_orders}')
# print('Finished sandwichs list :')
# for finished_sandwich in finished_sandwichs:
#     print(f'- {finished_sandwich} sandwich')

# ex.7.10
respones = {}
while True:
    name = input('Input you name:')
    name = name.lower()
    name = name.title()
    country = input(f'Which country would you like to go to {name}?:')
    country = country.lower()
    country = country.title()
    respones[name] = country
    cont_respones = input(f'Whould you like to continue respones(y/n)?:')
    if cont_respones == 'n':
        print('Responses:')
        for respon in respones.keys():
            print(f'{respon} wants to visit the {respones[respon]}.')
        break
    else:
        continue