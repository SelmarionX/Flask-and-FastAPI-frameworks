from flask import Flask, render_template
from forms import RegistrationForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'


@app.route('/', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        return render_template('success.html')
    return render_template('register.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
