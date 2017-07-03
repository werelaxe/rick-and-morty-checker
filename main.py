from concurrent.futures import ProcessPoolExecutor
from webserver import app
from content_downloader import download_content
from time import sleep


def update_content():
    while True:
        download_content()
        sleep(180)


def start_webserver():
    app.run()


def main():
    with ProcessPoolExecutor(2) as process_handler:
        process_handler.submit(update_content)
        process_handler.submit(start_webserver)


if __name__ == '__main__':
    main()
