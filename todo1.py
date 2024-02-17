import os
import time

todo = [] 

def saveTodoList():
    print('Saving Data')
    save_file = open('todo.save','w')
    for item in todo:
        save_file.write(item+'\n')
    save_file.close()



def loadTodoList():
    file_read = open('todo.save','r')
    lines = file_read.readlines()
    #print(lines)
    for line in lines:
        line = line.strip()
        todo.append(line)
    file_read.close()


def main():
    loadTodoList()
    while True:
        os.system('cls')
        print('1-Add a task')
        print('2-Delete a task')
        print('3-List all tasks')
        print('4-Save data')
        print('5-EXIT')
        ans = input('Your choice?:  ')
        if ans == '1':
            print('Adding a task')
            print('==============')
            task = input('Enter a task: ')
            todo.append(task)

        elif ans == '2':
            print('TaskList')
            print('=========')
            count = 0
            for t in todo:
                count = count + 1
                print(f'{count} - {t}')
            d = input('Which one to delete: ')
            d = int(d)
            del todo[d-1]

            print('Updated task list')
            print('==============')
            count = 0
            for t in todo:
                count = count + 1
                print(f'{count} - {t}')
        
        elif ans == '3':
            print('TaskList')
            print('=========')
            count = 0
            for t in todo:
                count = count + 1
                print(f'{count} - {t}')

        elif ans == '4':
            saveTodoList()
            time.sleep(4)
            print('Saved....')
            
        
        elif ans == '5':
            print('Bye')
            saveTodoList()
            exit(0)
        
        input('Press ENTER to continue...')





if __name__ == '__main__':
    main()

