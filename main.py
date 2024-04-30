import random
import time


def dummy_model():
    seed = random.random()
    if (int(seed * 10) % 3 == 0):
        return "right"
    elif (int(seed * 10) % 3 == 1):
        return "left"
    else:
        return None


while True:
    print(
        dummy_model())
    time.sleep(0.1)  # 10fps
