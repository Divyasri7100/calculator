from flask import Flask, render_template
import subprocess
import sys
import os

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/simple")
def launch_simple():
    subprocess.Popen([sys.executable, os.path.join("scripts", "simple.py")])
    return "Simple Calculator launched on the server!"

@app.route("/interest")
def launch_interest():
    subprocess.Popen([sys.executable, os.path.join("scripts", "newint.py")])
    return "Interest Calculator launched on the server!"

@app.route("/percentage")
def launch_percentage():
    subprocess.Popen([sys.executable, os.path.join("scripts", "newper.py")])
    return "Percentage Calculator launched on the server!"

@app.route("/EMI")
def launch_emi():
    subprocess.Popen([sys.executable, os.path.join("scripts", "newemi.py")])
    return "EMI Calculator launched on the server!"

@app.route("/EB")
def launch_electric_bill():
    subprocess.Popen([sys.executable, os.path.join("scripts", "neweb.py")])
    return "Electric Bill Calculator launched on the server!"

@app.route("/unit")
def launch_unit_conversion():
    subprocess.Popen([sys.executable, os.path.join("scripts", "newunitv.py")])
    return "Unit Conversion Calculator launched on the server!"

@app.route("/GST")
def launch_gst():
    subprocess.Popen([sys.executable, os.path.join("scripts", "newgst.py")])
    return "GST Calculator launched on the server!"

if __name__ == "__main__":
    app.run(debug=True)
