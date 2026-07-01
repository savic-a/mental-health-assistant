from nlp import chat

def option():
    # while True:
    print('1 - Chat')
    print('2 - Upload PDF')
    # print('3 - Exit')
    option = input('>> ')

    if option == '1':
        chat.start_chat()
    

