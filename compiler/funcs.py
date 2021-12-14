# CITF Compiler ---------------------------------------------------------------------------
# Here we have the CITF Compiler. Here is some things that you can customize to make a new
# CITF based custom compiler

# SETTINGS --------------------------------------------------------------------------------------------
# change here the keywords, special chars, and more for your new compiler (if you want, of course)

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



# IMPORTATIONS -----------------------------------------------------------
# don't change anything here

from colorama import Fore, init
import sys,os
init(autoreset=True)


# IMPORTANT VARS ---------------------------------------------------------
# don't change anything here

__tokens__ = []
__variables__ = []
__constants__ = []
__citf__ = str(os.getcwd())
__filename__ = ""
__destination__ = ""



# CLASSES ----------------------------------------------------------------
# don't change anything here

class Token:
    def tokenize(value, type):
        pass

class Error:
    def __init__(self, message):
        return print(Fore.RED+"(COMPILER ERROR) "+Fore.WHITE+"{}".format(str(message)))



# FUNCTIONS --------------------------------------------------------------
# don't change anything here, just change if you know what are you doing

def compile(f):
    __filename__ =  f
    __destination__= os.path.dirname(os.path.realpath(__filename__))

    if os.getcwd() == __citf__:
        os.chdir(os.getcwd()+'/compiler')
        os.mkdir('cenv')
        os.chdir(os.getcwd()+'/cenv')
        os.mkdir('build')