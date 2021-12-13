from colorama import Fore, init
import os, sys

SETTINGS={
    'keywords': [],
    'slash': [],
    'special': [],
    'types': [],
    'reserved': {},
    'allowUpper': False
}

init(autoreset=True)

def compile(f):
    return print("""Compiling {}\n
CITF Options: \n{}""".format(f,SETTINGS))