# CITF Compiler -----------------------------------------------------------------
# Here is the file for the configuration of CITF Compiler. Don't change anything
# if you don't know what are you doing.

from colorama import Fore
import json, os, shutil

# SETTINGS ----------------------------------------------------------------------
# Change here the reserved words and symbols for CITF, if you want.

SETTINGS={
    'keywords': [],
    'types': [],
    'declaration': ['const', 'let'],
    'specialChars': {
        'doubleQuotes': '"',
        'leftParen': '(',
        'rightParen': ')',
        'leftBracket': '[',
        'rightBracket': ']',
        'plus': '+',
        'minus': '-',
        'div': '/',
        'times': '*',
        'greater': '>',
        'less': '<',
        'and': '&',
        'or': '|',
        'not': '!',
        'equal': '==',
        'exactly': '===',
        'not_equal': '!=',
        'not_exactly': '!==',
        'end': ';'
    }
}



# ERROR ----------------------------------------------------------------------------
# don't change anything here

class Error:
    def __init__(self, message):
        return print(Fore.RED+"(ERROR) "+Fore.WHITE+f"{str(message)}")



# CONSTS ---------------------------------------------------------------------------
# don't change anything here

COMPILER_PATH = os.path.dirname(os.path.realpath(__file__))
CUR_PATH = str(os.getcwd())
CENV = "cenv"
EXAMPLES_PATH = "examples"

# COMPILE --------------------------------------------------------------------------
# don't change anything here

def compile(f):
    if "\citf" in CUR_PATH and "\citf\compiler" in COMPILER_PATH:

        # MAKING cenv

        os.chdir(CUR_PATH+"\compiler")

        if os.path.isdir(os.getcwd()+f"\{CENV}"):
            os.rmdir(CENV)
            os.mkdir(CENV)
        else: os.mkdir(CENV)

    else:
        return Error("CITF Path not found")