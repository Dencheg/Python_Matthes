# ex.8.12
# def sandwich_list(*toppings):
#     """sandwich topping list"""
#     text = f'Topping for sandwich:\n'
#     for topping in toppings:
#         text += f"- {topping}\n"
#     return text

# slist_1 = sandwich_list('chiken')
# print(slist_1)

# slist_2 = sandwich_list('chiken', 'cheese')
# print(slist_2)

# slist_3 = sandwich_list('butter', 'jam', 'ham')
# print(slist_3)

# ex.8.13
# def build_profile(name, surname, **profile):
#     """build user profile"""
#     profile['name'] = name
#     profile['surname'] = surname
#     return profile

# rprofil = build_profile('Sam', 'Winchester',
#                         age = '30',
#                         hight = '190',
#                         weight = '90')

# i = 1
# for key, value in rprofil.items():
#     print(f'{i}) {key} - { value}')
#     i +=1

# ex.8.14
def auto_profile(brand, color, **car_profil):
    car_profil['brand'] = brand
    car_profil['color'] = color
    return car_profil

car_profile_1 = auto_profile('geguli', 'green',
                             year = '2016',
                             number_wheels = 'four',
                             steering_wheel = 'one')
print(car_profile_1)