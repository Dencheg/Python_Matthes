# ex.4.10
pizzas_list = ['pepperoni', 'cheesy', 'banana', 'sausage', 'tomato']
print(f'I like pizza (first three points)"{pizzas_list[:3]}".')
print(f'I like pizza (middle three points)"{pizzas_list[1:4]}".')
print(f'I like pizza (last three points)"{pizzas_list[2:]}".')
print()

# ex.4.11
my_pizzas_list = ['pepperoni', 'cheesy', 'banana']
friend_pizzas_list = my_pizzas_list[:]
friend_pizzas_list.append('sausage')
print(f'Pizza im like: "{my_pizzas_list}".')
print(f'Pizza my friend like: "{friend_pizzas_list}".')
print()

# ex.4.12
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
my_foods.append('cannoli')
friend_foods.append('ice cream')
print('My favorite foods are:')
for my_food in my_foods:
    print(f'- {my_food}')
print('Friend favorite foods are:')
for friend_food in friend_foods:
    print(f'- {friend_food}')

# ex.x
pizzas_list = ['pepperoni', 'cheesy', 'banana', 'sausage', 'tomato']
print(pizzas_list[0:4:2]) 
print(pizzas_list[0:4:3])