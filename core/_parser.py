from core._sanitizer import Sanitizer
from core._tokenizer import Tokenizer


class Parser:

    def __init__(self, **kwargs):
        self._params = kwargs
        self._builtin = {}
        self._userdef = {}
        self._variables = {}
        # self._kernel = Kernel()
        # self._kernel.load_builtin('print', print)
        # self._kernel.load_builtin('input', input)
        # self._kernel.load_builtin('int', int)

    def parse(self, code: str, **kwargs):
        """Parse a code string."""
        self._code = Sanitizer(code).get_clean_data()
        self._tokens = Tokenizer(self._code).get_tokens()

        print(self._tokens)
