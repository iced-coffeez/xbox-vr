#!/bin/python3

from simple_websocket import ConnectionClosed
from flask import Flask, render_template
from flask_sock import Sock
import headset

f = None
read = None

gm = False

app = Flask(__name__)

app.config["SOCK_SERVER_OPTIONS"] = {
        "ping_interval": 25
}

app.config["TEMPLATES_AUTO_RELOAD"] = True

sock = Sock(app)

@app.route("/")
def index():
    return render_template("index.html")

@sock.route("/sock")
def websocket(ws):
    print("WebSocket go brr")

    ws.send("prep_site")
    
    try:
        while True:
            message = ws.receive(timeout=0)

            data = read.read(64)

            ws.send(data)
        
            if message == "webInit_PSVR":
                ws.send("Initializing PSVR 1...")
                headset.psvrControl = f
                headset.start()

            if message == "enable_gameMode":
                gm = True
                ws.send("Game Mode enabled... Headset will not turn off on disconnect.")

            if message == "disable_gameMode":
                gm = False
                ws.send("Game Mode disabled... Headset will turn off on disconnect.")

            print("Browser:", message)
    except ConnectionClosed:
        print("WebSocket disconnected")
        if gm == False:
            headset.turn_off()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)
