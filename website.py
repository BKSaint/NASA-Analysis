from flask import Flask, render_template, request, redirect, send_from_directory, abort
from flask_login import LoginManager, login_required, login_user, current_user, logout_user
import pymysql
import pymysql.cursors
from PIL import Image
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from collections import *




app = Flask(__name__)

@app.route("/")
def branch():

    return render_template("main.html.jinja")


if __name__ == '__main__':
    app.run(debug=True)