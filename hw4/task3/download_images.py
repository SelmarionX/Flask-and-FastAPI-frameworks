# Запускаем из терминала: python download_images.py https://kartinki.pics/uploads/posts/2022-02/1644872517_1-kartinkin-net-p-k
# otiki-kartinki-1.jpg


import time
import requests
import argparse
from concurrent.futures import ThreadPoolExecutor


def download_image(url):
    start_time = time.time()
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.HTTPError as http_err:
        print(f'Произошла ошибка HTTP: {http_err}')
    except Exception as err:
        print(f'Произошла другая ошибка: {err}')
    else:
        file_name = url.split("/")[-1]
        with open(file_name, "wb") as file:
            file.write(response.content)
        end_time = time.time()
        print(f"{file_name} скачано за {end_time - start_time} секунд")


def main(urls):
    start_time = time.time()
    with ThreadPoolExecutor() as executor:
        executor.map(download_image, urls)
    end_time = time.time()
    print(f"Общее время выполнения: {end_time - start_time} секунд")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("urls", nargs="+", help="URL-адреса изображений")
    args = parser.parse_args()
    main(args.urls)
