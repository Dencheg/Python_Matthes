# ex.8.16
def summa_divide(var_1, var_2, var_3):
    """sum two variables an divide by third"""
    text = f'({var_1} + {var_2}) / {var_3}'
    s_d = (int(var_1) + int(var_2)) / int(var_3)
    text += f' = {str(s_d)}'
    return text