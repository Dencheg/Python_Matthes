# ex.9.6
# class Restaurant():
#     """
#     description of restaurant and its cuisine
#     """
#     def __init__(self, restaurant_name, cuisine_type):
#         """
#         initializes attributes of restaurant
#         """
#         self.restaurant_name = restaurant_name
#         self.cuisine_type = cuisine_type

#     def open_restauraunt(self):
#         """display a message that the open a restaurant"""
#         print(f'!!!"{self.restaurant_name}" is OPEN!!!')


#     def discribe_restaurant(self):
#         """indicates a type of cuisine and  name of restaurant"""
#         print(f'Us restaurant "{self.restaurant_name.upper()}"')
#         print(f'THE BEST restaurant {self.cuisine_type} cuisine!')

# class IceCreamStand(Restaurant):
#     """description child restaurant class"""
#     def __init__(self, restaurant_name, cuisine_type):
#         """initializes attributes of restaurant
#            IceCreamStand 
#         """
#         super().__init__(restaurant_name, cuisine_type)
#         self.flavors = ['strawberry', 'blueberry', 'vanila']

#     def ice_flavors(self):
#         """lists ice cream flavors"""
#         text = f'We have next flavors:\n'
#         for flavor in self.flavors:
#             text += f'- {flavor}\n'
#         return text

# restaurant_1 = IceCreamStand('Frozen Throne', 'icy')
# restaurant_1.open_restauraunt()
# restaurant_1.discribe_restaurant()
# print(restaurant_1.ice_flavors())

# ex.9.7
class User():
    """user profil with a summari information"""

    def __init__(self, first_name, last_name, age='', level=''):
        """initializes attributes of user"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.level = level

    def greet_user(self):
        """displays a personal greeting for user"""
        if self.first_name == 'admin' and self.last_name == 'admin':
            print('Wellcome back mr. Neo *||||')
            print('v^v^v^v^v^v^v^v^v^v^v^v^v^')
        else:
            print(f'Hello {self.first_name}!')

    def discribe_user(self):
        """discribe summary information of user"""
        print('User information:')
        print(f'- name: {self.first_name}\n- surname: {self.last_name}')
        if self.age != '' and self.age != '':
            print(f'- age: {self.age}\n- level: {self.level}')
            lev = int(self.level)
            if lev == 5:
                print(' /\\ ')
                print('<:)>')
                print(' vv ')
            else:
                pass
        else:
            pass
        print()

# ex.9.7 ##########################################################
# class Admin(User):
#         """admin profil with a summari information"""
#         def __init__(self, first_name, last_name, age='', level=''):
#             """initializes attributes of admin"""
#             super().__init__(first_name, last_name, age, level)
#             self.privelages = ['added message is permitted',
#                           'banning users is permitted',
#                           'delete users is permitted']
#             self.flag = False
        
#         def greet_user(self):
#             """displays a personal greeting for user"""
#             if self.first_name == 'admin' and self.last_name == 'admin':
#                 print('Wellcome back mr. Neo *||||')
#                 print('v^v^v^v^v^v^v^v^v^v^v^v^v^')
#                 self.flag = True
#             else:
#                 print('!!!ACCESS DENIDE!!!')

#         def discribe_user(self):
#             """discribe summary information of user"""
#             if self.flag:
#                 print('User information:')
#                 print(f'- name: {self.first_name}\n- surname: {self.last_name}')
#                 if self.age != '' and self.age != '':
#                     print(f'- age: {self.age}\n- level: {self.level}')
#                     lev = int(self.level)
#                     if lev == 5:
#                         print(' /\\ ')
#                         print('<:)>')
#                         print(' vv ')
#                     else:
#                         pass
#                 else:
#                     pass
#             else:
#                 print('!NOT USER INFORMATION!')
#         print()
                                

#         def show_privilages(self):
#             """showed admin privilages"""
#             if self.flag:
#                 i = 1
#                 print('Admin privilages:')
#                 for privilage in self.privelages:
#                     print(f'{i}) {privilage}')
#                     i += 1
#             else:
#                 print('!NOT PRIVILAGES INFORMATION!')

#########################################################
# 9.8
class Admin(User):
        """admin profil with a summari information"""
        def __init__(self, first_name, last_name, age='', level=''):
            """initializes attributes of admin"""
            super().__init__(first_name, last_name, age, level)
            self.privelages = ['added message is permitted',
                          'banning users is permitted',
                          'delete users is permitted']
            self.flag = False
            self.privelages = Privelages(self.flag, self.privelages)
        
        def greet_user(self):
            """displays a personal greeting for user"""
            if self.first_name == 'admin' and self.last_name == 'admin':
                print('Wellcome back mr. Neo *||||')
                print('v^v^v^v^v^v^v^v^v^v^v^v^v^')
                self.flag = True
                self.privelages.flag = True
            else:
                self.flag = False
                self.privelages.flag = False
                print('!!!ACCESS DENIDE!!!')

        def discribe_user(self):
            """discribe summary information of user"""
            if self.flag:
                print('User information:')
                print(f'- name: {self.first_name}\n- surname: {self.last_name}')
                if self.age != '' and self.age != '':
                    print(f'- age: {self.age}\n- level: {self.level}')
                    lev = int(self.level)
                    if lev == 5:
                        print(' /\\ ')
                        print('<:)>')
                        print(' vv ')
                    else:
                        pass
                else:
                    pass
            else:
                print('!NOT USER INFORMATION!')
        print()

class Privelages():
    """information of user privelages"""
    def __init__(self, flag, privilages):
        """initializes attributes privelages"""
        self.flag = flag
        self.privilages = privilages

    def show_privilages(self):
        """showed admin privilages"""
        if self.flag:
            i = 1
            print('Admin privilages:')
            for privilage in self.privilages:
                print(f'{i}) {privilage}')
                i += 1
        else:
            print('!NOT PRIVILAGES INFORMATION!')
#########################################################

user_0 = Admin('admin', 'admin')
user_0.greet_user()
user_0.discribe_user()   
# user_0.show_privilages() # for # 9.7
user_0.privelages.show_privilages()

print()
user_1 = Admin('admin1', 'admin')
user_1.greet_user()
user_1.discribe_user()   
# user_1.show_privilages()  # for # 9.7
user_1.privelages.show_privilages()