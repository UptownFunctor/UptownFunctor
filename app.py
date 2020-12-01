from flask import Flask, render_template, url_for, session, redirect
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config['SECRET_KEY'] = '~3A;h@&a\d7'

bootstrap = Bootstrap(app)

@app.route('/')
def hello_world():
    return render_template("index.html")

@app.route('/delimiter_remover')
def delimiter_remover():
    return render_template("delimiter_remover.html")

@app.route('/hotdog')
def hotdog():
    return render_template("hotdog.html")


if __name__ == '__main__':
    app.run()
