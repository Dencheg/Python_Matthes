# ex.8.15
import ex_8_15_mod as ex
from ex_8_16_1_mod import summa
from ex_8_16_1_mod import divide as dvd, multiplecation as mltp 
from ex_8_16_2_mod import *

# inbox_list = ['Hello!', 'What you do?', 'I you like kiwi?']
# send_list = []
# ex.send_message(inbox_list, send_list)
# ret = ex.show_message(send_list)
# print(ret)
# print(f'Inbox list: {inbox_list}')

# inbox_list = ['Hi!', 'Are you crazy?', 'I you like fog?'] # 8.11
# send_list = []
# ex.send_message(inbox_list[:], send_list)
# ret = ex.show_message(send_list)
# print(ret)
# print(f'Inbox list: {inbox_list}')

# ex.8.16
summ_1 = summa(1, 3)
print(summ_1)

divide_1 = dvd(5, 2)
print(divide_1)

multiplication_1 = mltp(7, 3)
print(multiplication_1)

example = summa_divide(7, 8, 2)
print(example)

# ex.8.17
# formatted recomendations are followed