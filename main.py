from pathlib import Path
import headset
import webserver
import morse
import leds

vr = "psvr"


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

if (vr.lower() == "psvr"):
    psvrControl = open(find_hidraw(5), "wb", buffering=0)
    psvrRead = open(find_hidraw(4), "rb", buffering=0)

    headset.psvrControl = psvrControl
    
    webserver.f = psvrControl
    webserver.read = psvrRead
    webserver.app.run(host="0.0.0.0", port=80, debug=True)
