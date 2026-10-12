# ex.3.4
invite_list = ['Don Karleone', 'Piter Parker', 'Snusmumrik']
for i in range(0, len(invite_list)):
    print(f'Im invite you to lunch sir.{invite_list[i]}.')

# ex.3.5
popped_name = invite_list.pop(1)
print(f'{popped_name} want be able to come.')
new_people_0 = "Bruce Benner"
print(f"{new_people_0} will come.")
invite_list.insert(1, new_people_0)
for i in range(0, len(invite_list)):
    print(f'Im invite you to lunch sir.{invite_list[i]}.')

# ex.3.6
print('Im bought new table. Im may invited more guestes')
new_people_1 = "John Karter"
new_people_2 = "Donald Duck"
new_people_3 = "Ant"
invite_list.insert(0, new_people_1)
print(f"{new_people_1} will come.")
invite_list.insert(2, new_people_2)
print(f"{new_people_2} will come.")
invite_list.append(new_people_3)
print(f"{new_people_3} will come.")
for i in range(0, len(invite_list)):
    print(f'Im invite you to lunch sir.{invite_list[i]}.')

# ex.3.7
print("The table collapsed. There is room for only two guest at the table")
while len(invite_list) > 2:
    popped_name = invite_list.pop()
    print(f'Sorry {popped_name}, but invitation is canceled.')
for name in invite_list:
    print(f'You invitation {name}, still stands.')
del invite_list[1]
del invite_list[0]
print(invite_list)