# ex.9.11
from user_mod import User
from privelages_mod import Privelages

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