import time
import leds

# f = open("/dev/hidraw1", "wb", buffering=0)
f = None

off = bytes([
    0x15, 0x00, 0xaa, 0x10,
    0xff, 0x01,
    0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0
])

on = bytes([
    0x15, 0x00, 0xaa, 0x10,
    0xff, 0x01,
    100, 100, 100, 100, 100, 100, 100, 100, 100,
    0, 0, 0, 0, 0
])

def morse():
    leds.f = f

    leds.fadeInOut(.2)
    leds.fadeInOut(.2)
    leds.fadeInOut(.2)
    leds.fadeInOut(.6)
    time.sleep(.2)
    leds.fadeInOut(.2)
    leds.fadeInOut(.3)
    leds.fadeInOut(.2)

def morse_old():
    f.write(off)
    f.write(on)
    time.sleep(.1)
    f.write(off)
    time.sleep(.1)
    f.write(on)
    time.sleep(.1)
    f.write(off)
    time.sleep(.1)
    f.write(on)
    time.sleep(.1)
    f.write(off)
    time.sleep(.1)
    f.write(on)
    time.sleep(.3)
    f.write(off)
    time.sleep(.3)
    f.write(on)
    time.sleep(.1)
    f.write(off)
    time.sleep(.1)
    f.write(on)
    time.sleep(.3)
    f.write(off)
    time.sleep(.1)
    f.write(on)
    time.sleep(.1)
    f.write(off)
