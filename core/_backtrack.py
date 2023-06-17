"""
Backtracking a way to raise an exception.
"""

import sys
import traceback


class BacktrackException(Exception):
    """
    Exception to raise when backtracking.
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize the exception.
        """
        super(BacktrackException, self).__init__(*args, **kwargs)
        self.traceback = traceback.format_exc()

    def __str__(self):
        """
        Return the traceback.
        """
        return self.traceback
