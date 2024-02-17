import os

while True:
    os.system('cls')
    print('1- open file')
    print('2- save file')
    print('q- exit')
    ans = input('your choice: ')

    if ans == '1':
        print('opening file')
    elif ans == '2':
        print('saving file')
    elif ans == 'q':
        print('bye')
        exit(0)
    
    input('press Enter to continue....')