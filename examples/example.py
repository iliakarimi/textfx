from textfx import typeeffect, scrameffect, wavetext, untypeeffect, unscrameffect, unwavetext, SpinnerLoading, GlitchLoading, ProgressBarLoading
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


with SpinnerLoading(message="Loading ", animation="⠋⠙⠸⠴⠦⠇", message_color="red", animation_color="blue", delay=0.1):
    sleep(5)

with ProgressBarLoading(message="Loading", barline='-', animation='#', length=20, message_color="yellow", animation_color=None, barline_color="green", delay=0.1):
    sleep(4)

with GlitchLoading(message="Loading...", delay=0.1, charset="#$%&*@!?", color="blue"):
    sleep(3)