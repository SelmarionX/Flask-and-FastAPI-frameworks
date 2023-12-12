from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def news():
    # Данные о новостях
    news_data = [
        {'title': 'Новость 1', 'description': 'Краткое описание новости 1', 'date': '2023-12-01'},
        {'title': 'Новость 2', 'description': 'Краткое описание новости 2', 'date': '2023-12-02'},
        {'title': 'Новость 3', 'description': 'Краткое описание новости 3', 'date': '2023-12-03'},
    ]

    # Передача данных в шаблон через контекст
    return render_template('news.html', news=news_data)


if __name__ == '__main__':
    app.run(debug=True)
