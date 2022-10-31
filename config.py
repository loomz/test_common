import sys
import getopt


def get_env():
    opts, args = getopt.getopt(sys.argv[1:], "he:", ["help", "env="])

    env = None
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print('main.py -e <env>')
            print('or: test_arg.py --env=<env>')
            sys.exit()
        elif opt in ("-e", "--env"):
            env = arg

    return env
