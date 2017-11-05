#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Flask, render_template, g, request
app = Flask(__name__)

f = open("example_values.txt","r")
lift_station = {
    "WWTP-VLV-001": True,
    "WWTP-VLV-002": True,
    "WWTP-VLV-003": True,
    "WWTP-VLV-004": True,
    "WWTP-VLV-005": True,
    "WWTP-VLV-006": True,
    "WWTP-FM-001": 0.0,
    "WWTP-FM-002": 0.0,
    "WWTP-FM-003": 0.0,
    "WWTP-FM-004": 0.0,
    "WWTP-P-001": 1.0,
    "WWTP-P-002": 1.0,
    "WWTP-ULS-001": 0.0,
    "WWTP-ULS-002": 0.0
}

@app.route("/do_math", methods=["GET"])
def do_math():
    print(lift_station, type(lift_station["WWTP-ULS-001"]))
    if(lift_station["WWTP-VLV-001"]):
        if(lift_station["WWTP-ULS-001"] < 0.95):
            lift_station["WWTP-ULS-001"] = lift_station["WWTP-ULS-001"] + lift_station["WWTP-FM-001"]*20/14000
        else:
            lift_station["WWTP-VLV-001"] = False
            return "failure"
    print('after 1')
    if((float(lift_station["WWTP-ULS-001"]) > 0)):
        if(lift_station["WWTP-VLV-002"] and lift_station["WWTP-VLV-004"]):
            lift_station["WWTP-ULS-002"] = lift_station["WWTP-ULS-002"] + lift_station["WWTP-FM-002"]*20/14000
            lift_station["WWTP-ULS-001"] = lift_station["WWTP-ULS-001"] - lift_station["WWTP-FM-002"]*20/14000

        if(lift_station["WWTP-VLV-003"] and lift_station["WWTP-VLV-005"]):
            lift_station["WWTP-ULS-002"] = lift_station["WWTP-ULS-002"] + lift_station["WWTP-FM-003"]*20/14000
            lift_station["WWTP-ULS-001"] = lift_station["WWTP-ULS-001"] -  lift_station["WWTP-FM-003"]*20/14000
    print('after 2')
    if(float(lift_station["WWTP-ULS-002"]) > 0.95):
        lift_station["WWTP-VLV-002"] = False
        lift_station["WWTP-VLV-003"] = False
        return "failure"
    print('after 3')
    if(lift_station["WWTP-ULS-002"] > 0):
        if(lift_station["WWTP-VLV-006"]):
            lift_station["WWTP-ULS-002"] = lift_station["WWTP-ULS-002"] - lift_station["WWTP-FM-004"]*20/14000

    return str(lift_station)




@app.route("/poll_new", methods=["GET"])
def poll_values():
    file_data = f.readline()
    pre_colon = file_data.split()
    for item in pre_colon:
        split_item = item.split(":")

        lift_station[split_item[0]] = float(split_item[1])
    return "success"

@app.route("/poll", methods=["GET"])
def poll():
    return str(lift_station)


@app.route("/update_valve", methods=["POST"])
def update_valve():
    valve = request.form['valve']
    lift_station[valve] = not lift_station[valve]
    return "success"

@app.route("/update_pump", methods=["POST"])
def update_pump():
    pump = request.form['pump']
    value = request.form['value']
    lift_station[pump] = value
    if(pump == "WWTP-P-001"):
        lift_station["WWTP-FM-002"] = lift_station["WWTP-FM-002"] * value
    if(pump == "WWTP-P-002"):
        lift_station["WWTP-FM-003"] = lift_station["WWTP-FM-003"] * value

    return "success"

#default homepage, routed from home and the base url
@app.route("/")
@app.route(u"/💩", methods=["GET"])
def home():
    return render_template('index.html', lift_station=lift_station)




#runs servlet, debug=true if you want to test running code
if __name__ == "__main__":
    app.run(debug=True)
