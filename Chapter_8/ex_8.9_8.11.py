# ex.8.9
# def show_message(mess_list):
#     '''Output message list'''
#     i = 0
#     return_mess=f'Message list:\n'
#     for mess in mess_list:
#         i += 1      
#         return_mess += f'{i}) {mess}\n'
#     return return_mess

# inbox_list = ['Hello!', 'What you do?', 'I you like kiwi?']
# ret = show_message(inbox_list)
# print(ret)

# ex.8.10 and 8.11
def send_message(out_mess, send_list):
    '''to sended message'''
    while out_mess:
        popped_mess = out_mess.pop(0)
        send_list.append(popped_mess)
    if out_mess is not True:
        print('Out message list is empty')
    else:
        print('Copy of the list may be used...')
    print('Message list is sended')

            
def show_message(mess_list):
    '''Output message list'''
    i = 0
    return_mess=f'Message list:\n'
    for mess in mess_list:
        i += 1      
        return_mess += f'{i}) {mess}\n'
    return return_mess

inbox_list = ['Hello!', 'What you do?', 'I you like kiwi?']
send_list = []
send_message(inbox_list, send_list)
ret = show_message(send_list)
print(ret)
print(f'Inbox list: {inbox_list}')

inbox_list = ['Hi!', 'Are you crazy?', 'I you like fog?'] # 8.11
send_list = []
send_message(inbox_list[:], send_list)
ret = show_message(send_list)
print(ret)
print(f'Inbox list: {inbox_list}')
