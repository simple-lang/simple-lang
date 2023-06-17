from core._kernel import Kernel

class Startup:
    """The main class for bootstraping."""

    def __init__(self, **kwargs):
        self._params = kwargs

    def launch(self):
        """Launch the kernel."""
        print("Bootstrapping...")
        kernel = Kernel()
        kernel.launch()
        print("Bootstrap complete.")
        