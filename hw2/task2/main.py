from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        number = request.form.get('number')
        if number:
            return redirect(url_for('result', number=number))
    return render_template('home.html')


@app.route('/result/<int:number>')
def result(number):
    squared_number = number ** 2
    return render_template('result.html', number=number, squared_number=squared_number)


if __name__ == '__main__':
    app.run(debug=True)
