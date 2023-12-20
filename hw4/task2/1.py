# используется requests для скачивания страниц и threading
# для создания отдельных потоков для каждой страницы.

import requests
import threading

urls = ['http://ya.ru', 'http://lenta.ru', 'http://gb.ru']


def download_url(url, file_name):
    response = requests.get(url)
    with open(file_name, 'wb') as f:
        f.write(response.content)


threads = []
for i, url in enumerate(urls):
    file_name = f'file_{i}.html'
    t = threading.Thread(target=download_url, args=(url, file_name))
    threads.append(t)
    t.start()

for t in threads:
    t.join()
