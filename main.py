import argparse


def base():
    print("Doing base check...")


def nova(args):
    instancid = args.instanceid
    node = args.node
    print(node, instancid)


# get args:
parser = argparse.ArgumentParser()

# 添加必填参数：base\nova\cinder...
parser_base = parser.add_argument("base", help="input an arg to run .")
args_base = parser.parse_args()
subparsers = parser_base.add_subparsers(help='sub-command help')
if args_base == "base":
    base()

# 添加子命令 nova
# parser_nova = subparsers.add_parser('--nova', help='sub help')
parser_nova.add_argument('--instanceid', '-uuid', help='instance uuid')
parser_nova.add_argument('--node', '-n', help="")
# 设置默认函数
parser_nova.set_defaults(func=nova)
# 执行函数功能
args = parser.parse_args()
args.func(args)
