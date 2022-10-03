def menu(options):

    opLens = [len(i) for i in options]
    opLen = max(opLens)
    line = '_' * (22 + opLen) + '\n'

    flag = False
    while flag == False:
        print('Enter an option from the menu: ')
        print(line)
        for i in range(len(options)):
            print(' ' * 10 + str(i) + '. ' + options[i])
        print(line)
        ch = input('Enter a number for your choice: ')
        try:
            ch = int(ch)
            options[ch]
        except:
            print('\nEnter only numbers from the menu. \n')
        else:
            flag = True

    return ch
