from page_parser import parse_content
from content_grabber import get_content
from pickle import dumps


def download_content():
    with open("current_table", "wb") as file:
        file.write(dumps(parse_content(get_content())))
