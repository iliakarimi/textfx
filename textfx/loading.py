import sys
import random
import itertools
import threading
from time import sleep
from termcolor import colored




class SpinnerLoading():
    """
    A simple and lightweight spinner loading class that uses text animations to display the waiting state.

    This loading runs in a separate Thread and can be easily used using the context manager (`with`).

    Features:
    - Display a message with the spinner animation
    - Ability to customize the animation characters (with any string of characters)
    - Auto-end and display the final message after the `with` block is finished
    - Suitable for CLI tasks and applications that need live feedback while waiting

    Parameters:
    - message (str): Message to display at the beginning of the loading (before the spinner)
    - animation (str): String of characters to create the spinning effect (displayed in a loop)
    - delay (float): Delay time between displaying each frame of the animation
    """    
    def __init__(self, message="Loading ", animation="⠋⠙⠸⠴⠦⠇", message_color=None, animation_color=None, delay=0.1):
        self.message = message
        self.animation = animation
        self.message_color = message_color
        self.animation_color = animation_color
        self.delay = delay
        self._done = False
        self._thread = None

    def _animate(self):
        for frame in itertools.cycle(self.animation):
            if self._done:
                break
            sys.stdout.write(f"\r{colored(self.message, self.message_color)}{colored(frame, self.animation_color)}")
            sys.stdout.flush()
            sleep(self.delay)


    def __enter__(self):
        self._done = False
        self._thread = threading.Thread(target=self._animate, daemon=True)
        self._thread.start()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._done = True
        self._thread.join()


class ProgressBarLoading():
    """
    A class for a reciprocating bar loading where a symbol (like # or ░) moves back and forth within the bar
    and creates a sense of dynamism and active loading.

    This loading can be used with the `with` statement and runs live in a separate Thread
    during the execution of the block.

    Features:
    - An animated bar where the animated character moves back and forth between the lines of the bar.
    - Fully customizable: animation type, bar background character, start and end message.
    - Non-blocking execution with Thread.
    - Suitable for CLI and text applications.

    Parameters:
    - barline (str): fixed bar character (default: '-')
    - animation (str): animated symbol (default: '#')
    - length (int): bar length (number of characters)
    - message (str): message when loading starts
    - delay (float): Delay time between animation frames (seconds)
    """
    def __init__(self, message="Loading", barline='-', animation='#', length=20, message_color=None, animation_color=None, barline_color=None, delay=0.1):
        self.length = length
        self.message = message
        self.animation = animation
        self.message_color = message_color
        self.animation_color = animation_color
        self.barline_color = barline_color
        self.barline = barline
        self.delay = delay
        self._done = False
        self._thread = None
        self._pos = 0
        self._dir = 1 

    def _animate(self):
        while not self._done:
            bar = [colored(self.barline, self.barline_color)] * self.length
            bar[self._pos] = colored(self.animation, self.animation_color)
            sys.stdout.write(f"\r{colored(self.message, self.message_color)}: [{''.join(bar)}]")
            sys.stdout.flush()
            sleep(self.delay)

            if self._pos == self.length - 1:
                self._dir = -1
            elif self._pos == 0:
                self._dir = 1
            self._pos += self._dir


    def __enter__(self):
        self._done = False
        self._pos = 0
        self._dir = 1
        self._thread = threading.Thread(target=self._animate, daemon=True)
        self._thread.start()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._done = True
        self._thread.join()


class GlitchLoading():
    """
    A typographic loading with a 'glitch' effect that creates a sense of encryption or hacking by randomly replacing some letters
    in the displayed text.

    This class also supports context manager and is very suitable for loading in a fantasy or artistic style.

    Features:
    - Dynamic and random change of part of the characters of the main text
    - A sense of encryption, hacking, or mysterious loading
    - Completely non-blocking (in a separate thread)
    - Ability to customize charset, speed, and end message

    Parameters:
    - text (str): The text to which the glitch effect will be applied
    - delay (float): The delay between frames (lower value = faster effect)
    - charset (str): The characters used for the glitch effect
    """
    def __init__(self, message="Loading...", delay=0.1, charset="#$%&*@!?", color=None):
        self.message = message
        self.delay = delay
        self.charset = charset
        self.color = color
        self._done = False
        self._thread = None

    def _animate(self):
        while not self._done:
            glitched = ''.join(
                char if random.random() > 0.2 else random.choice(self.charset)
                for char in self.message
            )
            sys.stdout.write(f"\r{colored(glitched, self.color)}")
            sys.stdout.flush()
            sleep(self.delay)


    def __enter__(self):
        self._done = False
        self._thread = threading.Thread(target=self._animate, daemon=True)
        self._thread.start()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._done = True
        self._thread.join()
