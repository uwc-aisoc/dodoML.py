from enum import Enum
from typing import List

from pynput.keyboard import Key, Controller


# Using Enum instead of String (which is used in earlier versions)
class KeyDecision(Enum):
    NONE = 0
    RESET = 1
    LEFT = 2
    RIGHT = 3


_key_map: List[Key] = [0, 0, Key.left, Key.right]

# TODO Keys
# INFO: Pynput does not feature a hold for x seconds
# feature but only press and release.
# Solution 1 (written below): Press down and before the next calculation cycle, reset.
# Solution 2: Multithreading.
# Solution 3: Ticking. Make a update function that gets called in a loop
# with a deltaTime argument to automatically release pressed keys.

_ctrl = Controller()


def keyboard_masher(inp: KeyDecision):
    if inp == KeyDecision.NONE:
        return
    elif inp == KeyDecision.RESET:
        _ctrl.release(Key.left)
        _ctrl.release(Key.right)
        return

    _ctrl.press(_key_map[inp.value])
