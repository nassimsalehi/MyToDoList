import sys
import getopt

def empty_list():

    try:
        file = open('ToDolist.txt', 'w')
        file.writelines(["", "", ""])
        file.close()

    except FileNotFoundError as fnfe:
        print(fnfe)

    argv = sys.argv[1:]

    try:
        opts, args = getopt.getopt(argv, "lar:c:")

    except getopt.GetoptError as err:
        print(err)

    for opt, arg in opts:
        try:
            if opt in ['-l']:
                print('No todos for today!')

        except getopt.GetoptError as err:
            print(err)

empty_list()