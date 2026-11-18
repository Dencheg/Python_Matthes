# ex.8.15
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