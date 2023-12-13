from flask import Flask, render_template, request, make_response, redirect, url_for

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        user = request.form['name']
        email = request.form['email']
        resp = make_response(redirect(url_for('welcome')))
        resp.set_cookie('user', user)
        resp.set_cookie('email', email)
        return resp
    return render_template('index.html')


@app.route('/welcome')
def welcome():
    user = request.cookies.get('user')
    return render_template('welcome.html', user=user)


@app.route('/logout')
def logout():
    resp = make_response(redirect(url_for('index')))
    resp.set_cookie('user', '', expires=0)
    resp.set_cookie('email', '', expires=0)
    return resp


if __name__ == '__main__':
    app.run(debug=True)
