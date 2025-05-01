def menu():
    state = ''

    while True and state != 'exit':            
        try:
            state = input('action> ')

            if state == 'exit':
                print('Closing the program')
                state = 'exit'
        except KeyboardInterrupt:
            state = 'exit'
            print('\nKeyboard Interrupt')