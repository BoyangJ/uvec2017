from flask import Flask, render_template, g, request
app = Flask(__name__)

f = open("example_values.txt","r")
current_index = 0
lift_station = {
    "valves": {
        "valve1": True,
        "valve2": True,
        "valve3": True,
        "valve4": True,
        "valve5": True,
        "valve6": True
    },
    "tanks": {
        "tank1": 0,
        "tank2": 0
    },
    "pumps": {
        "pump1": 0,
        "pump2": 0
    }
}

def poll_values():
    file_data = f.readline()
    pre_colon = file_data.split()
    values[pre_colon[0]] = pre_colon[1]
    return values

@app.route("/update", methods=["POST"])
def valve():

    return "success"


#default homepage, routed from home and the base url
@app.route("/")
@app.route("/home", methods=["GET"])
@app.route("/poll", methods=["GET"])
def home():
    values = poll_values()


    return render_template('index.html', pagetype=values)




#runs servlet, debug=true if you want to test running code
if __name__ == "__main__":
    app.run(debug=True)
