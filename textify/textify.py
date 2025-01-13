from time import sleep
import random
import string

def typeeffect(text, delay=0.3):
    """""
    This type of effect prints text character by character with a specific delay.

        This effect is commonly used to simulate manual typing.
    """""
    
    for tp in text:
        sleep(delay)
        print(tp, end='', flush=True)


def falltext(text, delay=0.1):
    
    """""
    The characters "fall" from above one by one until the text is complete.
    
        Similar to the rain effect in the movie The Matrix.
    """""

    output = [' ' for _ in text]
    while ' ' in output:
        index = random.choice([i for i, char in enumerate(output) if char == ' '])
        output[index] = text[index]
        print("\r" + ''.join(output), end='', flush=True)
        sleep(delay)


def scrameffect(text, delay=0.1):
    
    """""
    The characters are first displayed randomly 
    
        (such as irrelevant letters or symbols) and gradually transform into actual text.
    """""
    
    scrambled = list(''.join(random.choices(string.ascii_letters + string.punctuation, k=len(text))))
    for i in range(len(text) + 1):
        scrambled[:i] = text[:i]
        print("\r" + ''.join(scrambled), end='', flush=True)
        sleep(delay)


def wavetext(text, delay=0.1):
    
    """""
    The text moves in a wave-like manner, as if the characters are jumping up and down.
    """""
    
    for i in range(len(text)):
        wave = ''.join([char.upper() if idx == i else char.lower() for idx, char in enumerate(text)])
        print("\r" + wave, end='', flush=True)
        sleep(delay)
