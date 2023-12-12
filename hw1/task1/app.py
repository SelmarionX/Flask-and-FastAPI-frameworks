# app.py
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/category/<category>')
def category(category):
    return render_template('category.html', category=category)

@app.route('/product/<product>')
def product(product):
    return render_template('product.html', product=product)

if __name__ == '__main__':
    app.run(debug=True)