"""
The heart of the language. The kernel is responsible for loading and executing functions.
"""
class Kernel:
    """The base class for all kernels."""

    def __init__(self, **kwargs):
        self._params = kwargs

    def load_builtin(self, name):
        """Load a built-in functions into the kernel."""

    def load(self, name, func):
        """Load a function into the kernel."""

    def execute(self, name, *args, **kwargs):
        """Execute a function with given arguments."""

    def launch(self):
        """Launch the kernel."""

        # parser = Parser()
        # parser.parse('print("Hello, world!")')
