from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/data', methods=["GET", "POST"])
def data():
    if request.method == "GET":
        return '<h1 style="color: green">The Test Works!</h1>'
    elif request.method == "POST":
        post_data = request.get_json()
        to_return = {'status': 200, 'response': post_data}
        return jsonify(to_return)


if __name__ == '__main__':
    app.debug = True
    app.run()
