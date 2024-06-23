import pandas as pd
import numpy as np
import json
import constants


class DtPreprocess:
    def __init__(self, data):
        self.validDtypes = constants.validDtypes
        self.data = data
        self.dtype = None
        self.valid_charts = set()
        self.render_chart_types()

    def validate(self):
        try:
            if self.checkNotNull():
                for instance in self.validDtypes:
                    if isinstance(self.data, instance):
                        self.dtype = instance
                if not self.dtype:
                    self.dtype = None
                    raise TypeError("Expected type doesn't match the variable type. Expected builder types are "
                                    f"{self.validDtypes}. But got the builder with the type: {type(self.data)}")
            else:
                raise TypeError("Data is validated as null value. Kindly check the builder and pass the same.")
        except Exception as e:
            raise

    def getDtype(self):
        return self.dtype

    def checkNotNull(self):
        try:
            if isinstance(self.data, pd.DataFrame):
                return not self.data.empty or len(self.data) == 0 or len(self.data.index) == 0
            elif isinstance(self.data, np.ndarray):
                return not (self.data.ndim and self.data.size)
            elif isinstance(self.data, dict):
                return not bool(self.data)
        except Exception as e:
            raise Exception("Exception occurred while doing null check. Check the builder for nullability.")

    def render_chart_types(self):
        with open("chart_types.json", 'r') as file:
            data = json.load(file)

            for item in data:
                keys = item.keys()
                self.valid_charts.update(keys)

            self.valid_charts = list(self.valid_charts)
