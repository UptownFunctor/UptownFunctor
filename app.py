from flask import Flask, render_template, request, make_response, jsonify, session, redirect
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config['SECRET_KEY'] = '~3A;h@&a\d7'

bootstrap = Bootstrap(app)

@app.route('/')
def hello_world():
    return render_template("index.html")

@app.route('/delimiter_remover', methods=['GET','POST'])
def delimiter_remover():

    if request.method == 'POST':
        print("processing text")

        text = request.get_json()['value']
        print(text.strip())

        res = ' '.join(text.split(';')).strip()
        return make_response(jsonify({'message': res}), 200)
    else:
        return render_template("delimiter_remover.html")

@app.route('/hotdog')
def hotdog():
    return render_template("hotdog.html")

@app.route('/hidden')
def hidden():
    return render_template("hidden.html")

if __name__ == '__main__':
    app.run()
