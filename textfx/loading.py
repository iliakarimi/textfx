import sys
import itertools
import threading
from time import sleep

class Loading():
    def __init__(self, message="Loading ", animation="⠋⠙⠸⠴⠦⠇", end_message="Done!", delay=0.1):
        self.message = message
        self.animation = animation
        self.end_message = end_message
        self.delay = delay
        self._done = False
        self._thread = None

    def _animate(self):
        for frame in itertools.cycle(self.animation):
            if self._done:
                break
            sys.stdout.write(f"\r{self.message}{frame}")
            sys.stdout.flush()
            sleep(self.delay)
        sys.stdout.write(f"\r{self.end_message}\n")

    def __enter__(self):
        self._done = False
        self._thread = threading.Thread(target=self._animate, daemon=True)
        self._thread.start()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._done = True
        self._thread.join()

