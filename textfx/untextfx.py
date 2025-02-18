import random
import string
from time import sleep

def untypeeffect(text, delay=0.1):
    """
    This effect gradually erases text character by character with a specific delay.

    It simulates the process of manual text deletion, making it useful for interactive
    terminal applications, chatbots, or animations.
    """

    print(text, end='', flush=True)
    sleep(1)
    for _ in text:
        print("\b \b", end='', flush=True)  # Removes characters one by one
        sleep(delay)



def unfalltext(text, delay=0.1):
    """
    The characters "rise" one by one until the text disappears.
    
    Similar to an inverse fall effect, where letters vanish in a scattered manner.
    """

    output = list(text)
    while any(char != ' ' for char in output):
        index = random.choice([i for i, char in enumerate(output) if char != ' '])
        output[index] = ' '
        print("\r" + ''.join(output), end='', flush=True)
        sleep(delay)



def unscrameffect(text, delay=0.1):
    """
    The actual text gradually scrambles into random characters until it disappears.

    This effect creates a glitch-like transition where letters are replaced with
    random symbols before vanishing completely.
    """

    scrambled = list(text)
    for i in range(len(text) + 1):
        if i < len(text): 
            scrambled[i:] = random.choices(string.ascii_letters + string.punctuation + ' ', k=len(text) - i)
        print("\r" + ''.join(scrambled), end='', flush=True)
        sleep(delay)

    print("\r" + " " * len(text), end='', flush=True)



def unwavetext(text, delay=0.1):
    """
    The text starts in a wave-like pattern and gradually stabilizes into normal text.
    
    This effect gives the illusion of motion calming down over time.
    """

    for i in range(len(text), -1, -1):
        wave = ''.join([char.upper() if idx == i else char.lower() for idx, char in enumerate(text)])
        print("\r" + wave, end='', flush=True)
        sleep(delay)

