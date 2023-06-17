"""
Tokenizer section of the parser.
"""
class Tokenizer:

    def __init__(self, string: str, **kwargs):
        self._string: str = string
        self._params: dict = kwargs
        self._tokens: list = []
        self._tokenize()

    def _tokenize(self):
        """Tokenize the string."""
        self._tokens = self._string.split(' ')

    def get_tokens(self):
        """Get the tokens."""
        return self._tokens

    def __str__(self):
        return '<Tokenizer object>'
