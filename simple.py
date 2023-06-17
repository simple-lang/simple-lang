"""
Simple Language Interpreter
Author: Md. Almas Ali
Version: 0.0.1

"""

import argparse

from core._bootstrap import Startup
from core._parser import Parser

__version__ = '0.0.1'
__author__ = 'Md. Almas Ali'
__prog_name__ = 'Simple Language'

if __name__ == '__main__':
    # startup = Startup()
    # startup.launch()

    parser = argparse.ArgumentParser(__prog_name__)
    parser.add_argument('--interactive', '-i',
                        help='To launch interactive shell', action='store_true')

    args = parser.parse_args()

    if args.interactive:
        while True:
            _code = input('>>> ') # get input from user

            if _code == 'exit':
                break  # exit the shell

            _prog_parser = Parser() # create a parser object
            _prog_parser.parse(_code) # parse the code

    else:
        print('this') # TODO: implement this
