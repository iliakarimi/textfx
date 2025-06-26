from textfx import typeeffect, scrameffect, wavetext, untypeeffect, unscrameffect, unwavetext, Loading
from time import sleep
import time

def run_examples():
    print("Typing Effect:")
    typeeffect("Hello, world!", color="cyan", delay=0.1)
    time.sleep(1)

    print("\nScramble Effect:")
    scrameffect("Scrambled Text", delay=0.1)
    time.sleep(1)

    print("\nWave Text:")
    wavetext("Wave Text", delay=0.1)
    time.sleep(1)

    print("\nUntyping Effect:")
    untypeeffect("Erasing Text", delay=0.1)
    time.sleep(1)

    print("\nUnscramble Effect:")
    unscrameffect("Glitching Away", delay=0.1)
    time.sleep(1)

    print("\nUnwave Text:")
    unwavetext("Steadying Waves", delay=0.1)
    time.sleep(1)

if __name__ == "__main__":
    run_examples()


with Loading("در حال پردازش... "):
    sleep(3)