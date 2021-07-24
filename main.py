from flask import Flask, render_template


app = Flask(__name__)


def test_yield():
    i = 1
    while True:
        yield i
        i += 1


@app.route('/')
@app.route('/librarian')
def index():
    return render_template('main.html', user='librarian')


@app.route('/student')
def student():
    return render_template('main.html', user='student')


@app.route('/test')
def test():
    return render_template('test.html', it=test_yield())


if __name__ == '__main__':
    app.run()
