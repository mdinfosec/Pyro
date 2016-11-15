import time, random, os
from piglow import PiGlow

while True:
    rnd = random.SystemRandom()
    pi = PiGlow()

    i0 = rnd.randint(0, 255)
    f0 = rnd.randint(4, 6)
    fl0 = pi.colour(f0, i0)

    i1 = rnd.randint(0, 255)
    f1 = rnd.choice([2, 3, 8, 9, 14, 15])
    fl1 = pi.led(f1, i1)

    flame = rnd.choice([fl0, fl1])
    t = rnd.uniform(0.025, 0.075)
    time.sleep(t)
    pi.all(0)
