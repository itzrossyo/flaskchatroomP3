from flask import Flask, render_template, request, session, redirect
from flask_socketio import join_room, leave_room, send, SocketIO
import random
from string import ascii_uppercase

app = Flask(__name__)
app.config['SECRET_KEY'] = "f239f2aksf2fd£$@!@£@!$F4"
socketio = SocketIO(app)

rooms = {}
def generate_unique_code(length):


@app.route("/", methods=["POST", "GET"])
def home():
    if request.method == "POST":
        name = request.form.get("name")
        code = request.form.get("code")
        join = request.form.get("join", False)
        create = request.form.get("create", False)

        if not name:
            return render_template("home.html", error="Please enter a name.")

        if join != False and not code:
            return render_template("home.html", error="please enter a code.")

        room = code
        if create != False:
            room = generate_unique_code


if __name__ == '__main__':
    socketio.run(app, debug=True)
