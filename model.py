from keyboard import keyboard_masher, KeyDecision
import random
import time


def dummy_model():
    seed = random.random()
    if int(seed * 10) % 3 == 0:
        return KeyDecision.RIGHT
    elif int(seed * 10) % 3 == 1:
        return KeyDecision.LEFT
    else:
        return KeyDecision.NONE


# Seconds before keyboard reset thus next cycle.
CONST_DELAY = 1

while True:
    # Model shenanigans here
    final_key = dummy_model()
    keyboard_masher(final_key)
    time.sleep(CONST_DELAY)
    keyboard_masher(KeyDecision.RESET)
    # End of one cycle
