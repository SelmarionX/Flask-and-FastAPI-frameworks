# используется multiprocessing для создания отдельных процессов для каждой страницы.

import requests
from multiprocessing import Pool

urls = ['http://ya.ru', 'http://lenta.ru', 'http://gb.ru']


def download_url(url):
    response = requests.get(url)
    file_name = url.split('/')[-1] + '.html'
    with open(file_name, 'wb') as f:
        f.write(response.content)


def main():
    with Pool() as p:
        p.map(download_url, urls)


if __name__ == "__main__":
    main()
