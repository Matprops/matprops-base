from ..constants import checkNotNull


class Description:
    def __init__(self, description):
        self.ref = description
        self.type = None

        self.set_description()

    def set_description(self):
        if checkNotNull(self.ref):
            self.set_description_type()
        else:
            self.ref = None

    def set_description_type(self):
        if isinstance(self.ref, str):
            self.type = "str"
        elif isinstance(self.ref, list):
            self.type = "list"
        else:
            self.ref = None
            self.type = None
