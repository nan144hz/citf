from colorama import Fore, init
import funcs
import os
import sys

init(autoreset=True)

# --------------------------------------

class Error:
    def __init__(self, msg):
        return print(Fore.RED+'(ERROR) '+Fore.WHITE+'{}'
            .format(msg))


def cmd(cmd):
    if cmd=="--help" or cmd=="-h": return funcs.help()
    elif cmd=="--version" or cmd=="-v": return funcs.version()
    elif cmd=="--compile" or cmd=="-c": return funcs.compile()
    elif cmd=="--read" or cmd=="-r": return funcs.read()
    else: return Error("Unknown command ('{}')".format(cmd.replace("-", "")))

if not len(sys.argv) > 1: Error("Insert a command")
else: cmd(sys.argv[1])