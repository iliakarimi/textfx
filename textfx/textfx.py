import string
import random
from time import sleep
from termcolor import colored



def typeeffect(text, color=None, delay=0.1):
    """""
    This type of effect prints text character by character with a specific delay.

        This effect is commonly used to simulate manual typing.
    """""
    for tp in text:
        sleep(delay)
        print(colored(tp, color), end='', flush=True)


def scrameffect(text, color=None, delay=0.1):
    
    """""
    The characters are first displayed randomly 
    
        (such as irrelevant letters or symbols) and gradually transform into actual text.
    """""
    scrambled = list(''.join(random.choices(string.ascii_letters + string.punctuation, k=len(text))))
    for i in range(len(text) + 1):
        scrambled[:i] = text[:i]
        print("\r" + colored(''.join(scrambled), color), end='', flush=True)
        sleep(delay)


def wavetext(text, color=None, delay=0.1):
    
    """""
    The text moves in a wave-like manner, as if the characters are jumping up and down.
    """""
    for i in range(len(text)):
        wave = ''.join([char.upper() if idx == i else char.lower() for idx, char in enumerate(text)])
        print("\r" + colored(wave, color), end='', flush=True)
        sleep(delay)

