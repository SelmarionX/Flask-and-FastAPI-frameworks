from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    error = None
    if request.method == 'POST':
        age = request.form['age']
        if not age.isdigit() or int(age) < 0 or int(age) > 120:
            return redirect(url_for('error', message='Некорректный возраст'))
        else:
            return redirect(url_for('result', name=request.form['name'], age=age))
    return render_template('index.html', error=error)


@app.route('/error/<message>')
def error(message):
    return render_template('error.html', message=message)


@app.route('/result/<name>/<age>')
def result(name, age):
    return render_template('result.html', name=name, age=age)


if __name__ == '__main__':
    app.run(debug=True)
