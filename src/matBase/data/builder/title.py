from ..constants import checkNotNull


class Title:
    def __init__(self, title):
        self.title = title
        self.title_type = None

        self.set_title()

    def set_title(self):
        if checkNotNull(self.title):
            self.set_title_type()
        else:
            self.title = None

    def set_title_type(self):
        if isinstance(self.title, str):
            self.title_type = "str"
        elif isinstance(self.title, list):
            self.title_type = "list"
        else:
            self.title = None
            self.title_type = None
