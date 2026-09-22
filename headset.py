from pathlib import Path
import time
import subprocess
import morse
import leds

# can be PSVR. every other HMD is a WIP right now—and probably won't work unless they use the same communication as the PSVR.

vr = "psvr"

global psvrControl

vrMode = bytearray([
    0x23, 0x00, 0xaa, 0x04, 0x01, 0x00, 0x00, 0x00
])

def find_hidraw(interface):
    for hidraw in Path("/sys/class/hidraw").glob("hidraw*"):
            path = hidraw.resolve()

            for parent in [path, *path.parents]:
                interface_file = parent / "bInterfaceNumber"

                if interface_file.exists():
                    number = int(interface_file.read_text().strip(), 16)
                    if number == interface:
                        return "/dev/" + hidraw.name

    return None

def start():
    if (vr.lower() == "psvr"):
        print("Initializing PSVR 1...")
        # psvrControl = open("/dev/hidraw1", "wb", buffering=0)
        
        '''vrMode = bytearray([
            0x23, 0x00, 0xaa, 0x04, 0x01, 0x00, 0x00, 0x00
        ])'''

        vrMode[4] = 0x01

        psvrControl.write(vrMode)

        morse.f = psvrControl

        morse.morse()

        leds.f = psvrControl

        time.sleep(.5)

        leds.fadeIn()
        

def turn_off():
    if (vr.lower() == "psvr"):
        vrMode[4] = 0x00

        psvrControl.write(vrMode)

        leds.f = psvrControl
        leds.setAllTo(100)
        time.sleep(1)
        leds.runAnim()
