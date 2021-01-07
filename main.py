from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
@app.route('/librarian')
def index():
    return render_template('main.html', user='librarian')


@app.route('/student')
def student():
    return render_template('main.html', user='student')


if __name__ == '__main__':
    app.run()
