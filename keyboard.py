import random
import time

from pynput.keyboard import Key, Controller


input_mappings = {
    "right": Key.right,
    "left": Key.left

}

def dummy_model():
    seed = random.random()
    if (int(seed * 10) % 3 == 0):
        return "right"
    elif (int(seed * 10) % 3 == 1):
        return "left"
    else:
        return "none"
    
def keyboardMasher(inp, delay):
    keyboard = Controller()
    if (inp != "none"):
        keyboard.press(input_mappings[inp])
        time.sleep(delay)



CONST_DELAY = 0.1

while True:
    # Model shenanigans here
    final_key = dummy_model()

    keyboardMasher(final_key, CONST_DELAY)
    # End of one cycle
