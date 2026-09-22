# TL;DR ONE PASTE SETUP IN WORKS

# XBOX VR Info
## Intro
Hello, and welcome to this humble little project! I just thought about doing something like this a few years back, and then just forgot about it. I wanted to be able to fulfill the promise that Microsoft made back in the early days of the XBOX One—the promise of virtual reality. Now, I'm going to state this multiple times throughout the project, but... <u>**you do NOT need a modded console. This setup only requires some type of computer—preferably a Pi 4 or newer—and does NOT need any sort of modifications to your console! Soft or hard mods! NOT REQUIRED!**</u>

Anyway, enough yapping. Let's move to the project.
## Prerequisites - Hardware
So, you need some sort of computer that can provide:

- An HDMI output (optionally)
- USB
- Some cable to connect the VR.

## Prerequisites - Software
The computer needs to have:
- Python 3 (preferably >= 3)
- The `sudo` binary (or just make the script have root privileges, or allow it to access /dev/hidraw* and port :80)
- Linux (preferably some form of new-ish Debian)

## Optional Prerequisites

- Some computer knowledge
- Sanity
- Sleep

# Supported Headsets
Currently:

PSVR 1

# Setup
To do this, you need to clone the GitHub repository. You can achieve this by:  
```bash
git clone https://github.com/iced-coffeez/xbox-vr  
cd xbox-vr
```

After this, you will want to decide on which headset you want to use. Make sure it's supported (or just force it to be) and then change:  

"vr" in `main.py` and  
"vr" in `headset.py`  

After that, make sure you have pip installed—or just use the built-in Python version.  
You need to create a **venv** for the Python packages. A **venv** is just a directory where Python can put packages that don't interfere with your system.  

Do this by running:  
`python -m venv .venv`  

The **venv** will be hidden, because of the leading dot. You will need to run `ls -la` or look in a file manager to find it.  

You will need to activate the **venv** and install needed packages. You can do this in 2 ways:  

<code>source .venv/bin/activate  
python -m pip install pathlib simple_websocket flask flask_sock</code>  

Or:

<code>source .venv/bin/activate  
pip3 install pathlib simple_websocket flask flask_sock</code>  

If neither work, try using just `pip` instead—or vice versa. In either option.

# Running
Finally, you are ready to run XBOX VR—after all of that pain.  

After this, you will want to hook up your headset of choice (if its supported—or you could just force it to be if you write your own drivers for it).  

From the root of the project directory, run:  
`sudo python3 main.py # sudo is optional if you're root—it would be redundant.`
