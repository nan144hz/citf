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
    elif cmd=="--compile" or cmd=="-c":
        if not len(sys.argv) > 2:
            return Error("The 'compile' command requires a filename as argument")
        elif not os.path.isfile(sys.argv[2]):
            return Error("The file doesn't exist! ('{}')".format(sys.argv[2]))
        elif not os.path.splitext(sys.argv[2])[1] == ".citf":
            return Error("The extension of the file must be '.citf'")
        else:
            return funcs.compile(sys.argv[2])
    elif cmd=="--read" or cmd=="-r":
        if not len(sys.argv) > 2:
            return Error("The 'read' command requires a filename as argument")
        elif not os.path.isfile(sys.argv[2]):
            return Error("The file doesn't exist! ('{}')".format(sys.argv[2]))
        elif not os.path.splitext(sys.argv[2])[1] == ".citf":
            return Error("The extension of the file must be '.citf'")
        else:
            return funcs.read(sys.argv[2])
    else: return Error("Unknown command ('{}')".format(cmd.replace("-", "")))

if not len(sys.argv) > 1: Error("Insert a command")
else: cmd(sys.argv[1])