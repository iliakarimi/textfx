import string
import random
from time import sleep
from termcolor import colored




def untypeeffect(text, color=None, delay=0.1):
    """
    This effect gradually erases text character by character with a specific delay.

    It simulates the process of manual text deletion, making it useful for interactive
    terminal applications, chatbots, or animations.
    """
    print(colored(text , color), end='', flush=True)
    sleep(1)
    for _ in text:
        print("\b \b", end='', flush=True)  # Removes characters one by one
        sleep(delay)


def unscrameffect(text, color=None, delay=0.1):
    """
    The actual text gradually scrambles into random characters until it disappears.

    This effect creates a glitch-like transition where letters are replaced with
    random symbols before vanishing completely.
    """
    scrambled = list(text)
    for i in range(len(text) + 1):
        if i < len(text): 
            scrambled[i:] = random.choices(string.ascii_letters + string.punctuation + ' ', k=len(text) - i)
        print("\r" +colored(''.join(scrambled), color), end='', flush=True)
        sleep(delay)

    print("\r" + " " * len(text), end='', flush=True)


def unwavetext(text, color=None, delay=0.1):
    """
    The text starts in a wave-like pattern and gradually stabilizes into normal text.
    
    This effect gives the illusion of motion calming down over time.
    """
    for i in range(len(text), -1, -1):
        wave = ''.join([char.upper() if idx == i else char.lower() for idx, char in enumerate(text)])
        print("\r" + colored(wave, color), end='', flush=True)
        sleep(delay)
