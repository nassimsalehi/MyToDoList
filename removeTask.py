import sys
import getopt


def remove_task():

    my_index = None
    argv = sys.argv[1:]
    try:
        file = open('ToDoList.txt', "r")
        my_list = file.readlines()

    except FileNotFoundError as fnfe:
        print(fnfe)

    try:
        opts, args = getopt.getopt(argv, "lar:c:")
    except getopt.GetoptError as err:
        print(err)
        print('Unsupported argument')

    if len(my_list) >= 2:
        for opt,arg in opts:
            if opt in ['-r']:
                my_index = arg

                if my_index == 2:
                    try:
                        my_list.pop()
                        file = open('ToDoList.txt', "w")
                        file.writelines(my_list)
                        file.close()

                    except FileNotFoundError as fnfe:
                        print(fnfe)

                elif my_index == "":
                    print('Unable to remove: no index provided')

                elif len(my_list) < 20 and my_index == 20:
                    print('Unable to remove: index is out of bound')

                elif arg == 'apple':
                    print('Unable to remove: index is not a number')

            else:
                print('opt is not correct')
    else:
        print('my list dosnt have 2 more item')

remove_task()