#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Flask, render_template, g, request
app = Flask(__name__)

f = open("example_values.txt","r")
current_index = 0
lift_station = {
    "WWTP-VLV-001": True,
    "WWTP-VLV-002": True,
    "WWTP-VLV-003": True,
    "WWTP-VLV-004": True,
    "WWTP-VLV-005": True,
    "WWTP-VLV-006": True,
    "WWTP-FM-001": 0,
    "WWTP-FM-002": 0,
    "WWTP-FM-003": 0,
    "WWTP-FM-004": 0,
    "WWTP-P-001": 0,
    "WWTP-P-002": 0,
    "WWTP-ULS-001": 0,
    "WWTP-ULS-002": 0
}

@app.route("/poll", methods=["GET"])
def poll_values():
    file_data = f.readline()
    pre_colon = file_data.split()
    for item in pre_colon:
        split_item = item.split(":")
        lift_station[split_item[0]] = split_item[1]
    return "success"

@app.route("/update", methods=["GET"])
def valve():
    return lift_station


#default homepage, routed from home and the base url
@app.route("/")
@app.route(u"/💩", methods=["GET"])
def home():
    return render_template('index.html', lift_station=lift_station)




#runs servlet, debug=true if you want to test running code
if __name__ == "__main__":
    app.run(debug=True)
