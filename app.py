from MCP3008 import MCP3008
import time
from flask import Flask, render_template, jsonify


global start_time, stop_time, running_1, running_2

adc = MCP3008()

app = Flask(__name__)

@app.route("/start_run", methods=["POST"])
def start_run():
    global running_1, start_time, stop_time
    start_time = 0
    stop_time = 0
    running_1 = True
    while running_1 == True:
        if adc.read(channel = 0) < 400:
            start_time = start_clock()
            running_1 = False
            end_run()
    run_time = stop_time - start_time
    run_time = format(run_time, '.2f')
    if float(run_time) > 0:
        return run_time
    else:
        return " "

def end_run():
    global running_2, stop_time
    running_2 = True
    while running_2 == True:
        if adc.read(channel = 1) < 250:
            stop_time = stop_clock()
            running_2 = False

def start_clock():
    start_time = time.time()
    return start_time

def stop_clock():
    stop_time = time.time()
    return stop_time


@app.route("/reset_run", methods=["POST"])
def reset_run():
    global running_1, running_2
    running_1 = False
    running_2 = False
    return "stop"

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html", title="40 Yard Dash")
