import sys
sys.path.append("./modules")
from flask import Flask, render_template,request,redirect,url_for
import websocket
from binance.client import Client
from binance.enums import *

import bot
SOCKET = "wss://stream.binance.com:9443/ws/btcusdt@kline_5m"



closes = []
in_position = True


app = Flask(__name__)



@app.route("/")
def index():
    return render_template("index.html")

@app.route('/start')
def startBot():
    print("helooo")
    data = request.args
    client = Client(data['public_key'], data['private_key'], tld='us')
    ws = websocket.WebSocketApp(SOCKET, on_open=bot.on_open, on_close=bot.on_close, on_message=bot.elDon)
    ws.run_forever()
    
    
