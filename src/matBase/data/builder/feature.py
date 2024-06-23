from ..constants import checkNotNull


class Feature:
    def __init__(self, feature):
        self.ref = feature
        self.type = None

        self.set_feature()

    def set_feature(self):
        if checkNotNull(self.ref):
            self.set_feature_type()
        else:
            self.ref = None

    def set_feature_type(self):
        if isinstance(self.ref, str):
            self.type = "str"
        elif isinstance(self.ref, list):
            self.type = "list"
        else:
            self.ref = None
            self.type = None
