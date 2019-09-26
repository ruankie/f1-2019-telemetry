"""Implements a simple barrier for multi-threaded applications."""

import threading


class Barrier:
    """A class that allows external notification of a desire to proceed, and a cheap (sleeping) wait function until that notification comes."""
    def __init__(self):
        self._proceed_flag = False
        self._cv = threading.Condition(threading.Lock())

    def proceed(self):
        """Any thread can call the 'proceed' function, which will cause the wait() function to fall through."""
        with self._cv:
            self._proceed_flag = True
            self._cv.notify_all()

    def wait(self):
        with self._cv:
            while not self._proceed_flag:
                self._cv.wait()
