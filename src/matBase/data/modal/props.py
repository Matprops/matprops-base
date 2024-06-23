import pandas as pd
import numpy as np

from ..builder.feature import Feature


class Prop:
    def __init__(self, dtype, data, feature, title, description):
        self.data = dict()
        self.feature = feature
        self.title = title
        self.description = description

        if dtype == pd.DataFrame:
            self.evalDataFrame(data)
        elif dtype == np.ndarray:
            self.evalNpArray(data)
        elif dtype == dict:
            self.evalDict(data)

    def evalDataFrame(self, data):
        if self.feature.feature_type == "list" or self.description.description_type

    def evalNpArray(self, data):
        pass

    def evalDict(self, data):
        pass
