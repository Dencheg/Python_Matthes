# ex.9.10
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