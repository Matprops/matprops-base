from ..constants import checkNotNull, validate_type
import pandas as pd
from ...utils.common import eval_list, eval_dict


class Feature:
    def __init__(self, feature, ref):
        self.ref = ref
        self.feature = feature
        self.data = None

        self.type = None

        self.set_feature()

    def set_feature(self):
        self.type = validate_type(self.feature, self.ref)
        self.build_feature()

    def build_feature(self):
        if self.type == "list":
            if eval_list(self.data):
                self.data = pd.Series(self.data, name=self.ref)
        if self.type == "dict":
            if eval_dict(self.data):
                self.data = pd.Series(self.data, name=self.ref)


