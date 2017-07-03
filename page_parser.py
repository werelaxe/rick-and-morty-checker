from html.parser import HTMLParser


class NewEpisodesParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self._handling = False
        self._tables_count = 0
        self._collect_index = 0
        self.collected_lines = []

    def error(self, message):
        pass

    def handle_starttag(self, tag, attrs):
        if tag == "table":
            self._tables_count += 1
        if self._tables_count != 2:
            return
        if tag == "tr":
            self._handling = True

    def handle_endtag(self, tag):
        if self._tables_count != 2:
            return
        if tag == "tr":
            self._handling = False

    def handle_data(self, data):
        if self._handling:
            stripped_data = data.strip()
            if stripped_data != "":
                if "rick" in stripped_data.lower():
                    self._collect_index = 1
                    self.collected_lines.append([stripped_data])
                if not self._collect_index:
                    return
                self._collect_index += 1
                self.collected_lines[-1].append(stripped_data)
                if self._collect_index == 9:
                    self._collect_index = 0


def parse_content(content):
    parser = NewEpisodesParser()
    parser.feed(content)
    return parser.collected_lines
