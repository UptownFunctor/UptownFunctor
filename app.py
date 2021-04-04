from flask import Flask, render_template, request, make_response, jsonify, session, redirect
from flask_bootstrap import Bootstrap
from static.forms.delimiter_remover.delimiter_remover_forms import TextAreaForm
from blueprints.hotdog.hotdog_app import hotdog_app

app = Flask(__name__)
app.config['SECRET_KEY'] = '~3A;h@&a\d7'
app.config['MAX_CONTENT_LENGTH'] = 10 * 1024 * 1024 # Limit request object size to 10mb

app.register_blueprint(hotdog_app)

bootstrap = Bootstrap(app)

@app.route('/')
def hello_world():
    return render_template("index.html")

@app.route('/delimiter_remover', methods=['GET','POST'])
def delimiter_remover():
    form = TextAreaForm()

    if request.method == 'POST':
        print("processing text")

        text = request.get_json()['text']
        delimiter = request.get_json()['delimiter']

        d_len = len(delimiter)
        res = (''*d_len).join(text.split(delimiter)).strip()

        return make_response(jsonify({'message': res}), 200)
    else:
        return render_template("delimiter_remover.html", form=form)

@app.route('/hidden')
def hidden():
    return render_template("hidden.html")

if __name__ == '__main__':
    app.run()
