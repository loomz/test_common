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
            print('or: tmain.py --env=<env>')
            sys.exit()
        elif opt in ("-e", "--env"):
            current_env = arg

    assert current_env, "环境变量使用命令行参数 -e 或者 --env, 可选项为[test, pre, prd]，比如 python main.py --env test"

    return current_env
