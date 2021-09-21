from flask import Flask, render_template, request, redirect
import datetime

app = Flask(__name__)
logs = ""


@app.route('/')
def index():
    return render_template("index.html", logs=logs)


@app.route('/up', methods=["GET", "POST"])
def up():
    global logs
    logs += str(datetime.datetime.now().time()) + " --> Up\n"
    return redirect("/")


@app.route('/down', methods=["GET", "POST"])
def down():
    global logs
    logs += str(datetime.datetime.now().time()) + " --> Down\n"
    return redirect("/")


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
