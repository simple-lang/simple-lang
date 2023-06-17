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
            _code = input('>>> ')
            _prog_parser = Parser()
            _prog_parser.parse(_code)

    else:
        print('this')