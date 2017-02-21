from models import *
from flask import Flask, request, g, redirect, url_for, \
    render_template, flash

app = Flask(__name__)
app.config.from_object(__name__)


def init_db():
    db = CreateDatabase.create_db_object()
    db.connect()
    db.create_tables([Entries], safe=True)


@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'postgre_db'):
        g.postgre_db.close()


@app.route('/request-counter')
def request_counter():
    counter = 0
    counter += 1
    return redirect('/')









if __name__ == "__main__":
    init_db()
    app.run()
