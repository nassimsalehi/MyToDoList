import sys
import getopt


def todo_list():

    my_arg = None
    task_state = ['undone', 'done', 'undone']

    try:
        file_read = open('ToDolist.txt', 'r')
        task_list = file_read.readlines()
        file_read.close()
    except FileNotFoundError as fnfe:
        print('File Not Found!!!')

    argv = sys.argv[1:]

    try:
        opts, args = getopt.getopt(argv, "lar:c:")

    except getopt.GetoptError as err:
        print('Unsupported argument')
        print('check task')

    # list undone task
    for opt, arg in opts:
        if opt in ['-l']:
            for i in range(len(task_list)):
                if task_state[i] == 'undone':
                    sign = '[]'
                    print(str(i + 1) + '-' + sign + str(task_list[i]))
                elif task_state[i] == 'done':
                    sign = '[x]'
                    print(str(i + 1) + '-' + sign + str(task_list[i]))

        elif opt in ['-c']:
            my_arg = arg
            if arg != '':
                if len(task_list) >= 2:
                    try:
                        if int(my_arg) == 2:
                            print('check the second task from the file')
                        else:
                            print('Unable to check: no index provided')
                    except getopt.GetoptError as err:
                        print(err)

            else:
                print('Unable to check: no index provided')

        else:
            print('this is a command line todo list')

todo_list()