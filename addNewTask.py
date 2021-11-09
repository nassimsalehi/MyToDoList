import sys
import getopt



def add_new_task():

    task = ''
    argv = sys.argv[1:]

    try:
        opts, args = getopt.getopt(argv, "lar:c:")

    except getopt.GetoptError as err:
        print(err)
        print('Unsupported argument')

    for opt, arg in opts:

        try:
            if opt in ['-a']:
                if arg == "Feed the monkey":
                    try:
                        file = open('ToDoList.txt', 'a')
                        file.write('Feed the monkey')
                        file.close()
                        # 'Then it should add a new task with the description Feed the monkey'
                    except FileNotFoundError as fnfe:
                        print(fnfe)


        except getopt.GetoptError as err:
            print('Unable to add: no task provided')

add_new_task()