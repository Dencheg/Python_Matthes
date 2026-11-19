# ex.9.11
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