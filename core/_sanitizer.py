class Sanitizer:

    def __init__(self, string: str, **kwargs):
        self._string: str = string
        self._params: dict = kwargs
        self._sanitize()

    def _sanitize(self, **kwargs):
        """Sanitize the string."""
        self._string = self._string.strip()
        self._string = self._string.replace('\n', ' ')
        self._string = self._string.replace('\t', ' ')
        self._string = self._string.replace('\r', ' ')
        self._string = self._string.replace('  ', ' ')

    def get_clean_data(self):
        """Get the sanitized string."""
        return self._string

    def __str__(self):
        return '<Sanitizer object>'
