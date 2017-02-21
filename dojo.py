from models import *
from flask import Flask, request, g, redirect, url_for, \
    render_template


app = Flask(__name__)
app.config.from_object(__name__)

DEBUG = True


def init_db():

    print("qwidhqwiudqwiudq")
    try:
        db.connect()
        print("Database connection established.")
    except:
        print("Can't connect to database.\nPlease check your connection.txt file.")


@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'postgre_db'):
        g.postgre_db.close()

@app.route('/')
def main_menu():
    return render_template('dojo_menu.html')

@app.route('/request-counter')
def request_counter():
    counter = 0
    counter += 1
    return redirect('/')


if __name__ == "__main__":
    init_db()
    app.run(host='0.0.0.0')
