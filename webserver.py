from pickle import loads

import datetime
from flask import Flask, render_template
import time

app = Flask(__name__)
table = ""
last_update_time = ""


def get_server_time():
    current_time = int(time.time() - 4 * 60 * 60)
    return datetime.datetime.fromtimestamp(current_time).strftime('%m-%d %H:%M')


def update_table():
    global table
    global last_update_time
    with open("current_table", "rb") as table_file:
        try:
            content = table_file.read()
            table = loads(content)
            last_update_time = table[0][-3]
        except Exception:
            pass


@app.route("/")
def main_page():
    global last_update_time
    update_table()
    return render_template("main_page.html", last_update_time=last_update_time, current_time=get_server_time())


@app.route("/table")
def statistics():
    global table
    update_table()
    return render_template("table.html", table=table)
