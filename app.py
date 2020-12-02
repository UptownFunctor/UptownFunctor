from flask import Flask, render_template, request, make_response, jsonify, session, redirect
from flask_bootstrap import Bootstrap
from static.forms.delimiter_remover.delimiter_remover_forms import TextAreaForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '~3A;h@&a\d7'

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
        res = (' '*d_len).join(text.split(delimiter)).strip()

        return make_response(jsonify({'message': res}), 200)
    else:
        return render_template("delimiter_remover.html", form=form)

@app.route('/hotdog')
def hotdog():
    return render_template("hotdog.html")

@app.route('/hidden')
def hidden():
    return render_template("hidden.html")

if __name__ == '__main__':
    app.run()
