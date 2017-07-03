import requests

DOWNLOAD_URL = "https://kickass.cd/usearch/rick%20and%20morty/?field=time_add&sorder=desc"
HEADERS = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36"}


def get_content():
    return requests.get(DOWNLOAD_URL, headers=HEADERS).content.decode()
