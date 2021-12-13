from colorama import Fore

def help():
    print("""Syntax: citf """+Fore.LIGHTGREEN_EX+"""<command> [input files (if nescessary)]\n"""+Fore.WHITE+"""
    \t-h, --help | Shows this help message
    \t-v, --version  | Show the current version of CITF
    \t-c, --compile | Compiles a .citf file (it requires a filename as argument)
    \t-r, --read | Read and print the contents of a .citf file (it requires a filename as argument)""")

def version():
    return print("CITF Compile It in Files\n"+Fore.GREEN+"Version 1.0.0 Licensed under Apache 2.0 License")

def compile():
    pass

def read():
    pass