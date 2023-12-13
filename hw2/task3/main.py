from flask import Flask, render_template, request, flash, redirect, url_for
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        flash(f'Привет, {name}!')
        return redirect(url_for('message'))
    return render_template('index.html')


@app.route('/message')
def message():
    return render_template('message.html')


if __name__ == '__main__':
    app.run(debug=True)
