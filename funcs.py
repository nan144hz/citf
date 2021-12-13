from colorama import Fore
import compiler.funcs

def help():
    print("""Syntax: citf """+Fore.LIGHTGREEN_EX+"""<command> [input files (if nescessary)]\n"""+Fore.WHITE+"""
    \t-h, --help | Shows this help message
    \t-v, --version  | Show the current version of CITF
    \t-c, --compile | Compiles a .citf file (it requires a filename as argument)
    \t-r, --read | Read and print the contents of a .citf file (it requires a filename as argument)""")

def version():
    return print("CITF Compile It in Files\n"+Fore.GREEN+"Version 1.0.0 Licensed under Apache 2.0 License")

def compile(file):
    return compiler.funcs.compile(file)

def read(file):
    with open(file, 'r') as f:
        content = f.read()
        f.close()
        return print("""Content of the file """+Fore.LIGHTGREEN_EX+"""{}\n""".format(file)+Fore.WHITE+"\n"+
"""{}""".format(content))
