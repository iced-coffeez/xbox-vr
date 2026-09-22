import time

# f = open("/dev/hidraw1", "wb", buffering=0)

f = None

bestleds = bytearray([100, 100, 100, 100, 25, 5, 5, 10, 10])

leds = bytearray([100, 100, 100, 100, 100, 100, 100, 100, 100])
#                  A    B    C    D    E    F    G    H    I

pairs = [
    (2, 3),
    (5, 6),
    (0, 1),
    (7, 8),
]

delay = 20

payload = bytearray([
    0x15, 0x00, 0xaa,0x10,
    0xff,0x01,
    *leds,

    0, 0, 0, 0, 0
])

'''for i in range(len(leds)):
    leds[i] = max(0, leds[i] - 1)'''
    
# leds[:] = [100] * 9
def runAnim():
    f.write(payload)

    for frame in range(100 + delay * len(pairs)):
        for p, (a, b) in enumerate(pairs):
            start = p * delay

            if frame >= start:
                brightness = max(0, 100 - (frame - start))
                leds[a] = brightness
                leds[b] = brightness

        payload[6:15] = leds
        f.write(payload)
        time.sleep(0.02)

    for brightness in range(100, -1, -1):
        leds[4] = brightness

        payload[6:15] = leds
        f.write(payload)

        time.sleep(0.0125)

def fadeIn():
    for brightness in range(101):
        leds[:] = [brightness] * 9
        payload[6:15] = leds
        f.write(payload)
        time.sleep(0.02)

def setAllTo(value):
    leds[:] = [value] * 9
    payload[6:15] = leds
    f.write(payload)

def lerp(start, end, progress):
    return start + (end - start) * progress

def fadeInOut(duration):
    startTime = time.monotonic()

    while True:
        elapsed = time.monotonic() - startTime
        progress = elapsed / duration

        if progress >= 1:
            leds[:] = [0] * 9
            payload[6:15] = leds
            f.write(payload)
            break
        
        if progress < 0.5:
            brightness = int(lerp(0, 100, progress * 2))
        else:
            brightness = int(lerp(100, 0, (progress - 0.5) * 2))

        leds[:] = [brightness] * 9
        payload[6:15] = leds
        f.write(payload)

        time.sleep(0.01)
