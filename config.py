import sys
import getopt

current_env = None


def get_env():
    global current_env

    if current_env:
        return current_env

    print("sys.argv=%s" % sys.argv)
    opts, args = getopt.getopt(sys.argv[1:], "he:", ["help", "env="])

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print('main.py -e <env>')
            print('or: test_arg.py --env=<env>')
            sys.exit()
        elif opt in ("-e", "--env"):
            current_env = arg

    return current_env
