# ex.8.16
def summa(var_1, var_2):
    """sum two variables"""
    text = f'{var_1} + {var_2}'
    summ = int(var_1) + int(var_2)
    text += f' = {str(summ)}'
    return text

def multiplecation(var_1, var_2):
    """multiplecation two variables"""
    text = f'{var_1} * {var_2}'
    multip = int(var_1) * int(var_2)
    text += f' = {str(multip)}'
    return text

def divide(var_1, var_2):
    """divide two variables without a remainder"""
    text = f'{var_1} // {var_2}'
    div = int(var_1) // int(var_2)
    text += f' = {str(div)}'
    return text

