import pandas as pd
import json

from preprocess import DtPreprocess
from modal.props import Prop
from constants import checkNotNull, validate_type, validate_dataset
from builder.feature import Feature
from builder.title import Title
from builder.description import Description
from src.matBase.utils.common import get_function_stack


class MatData:
    def __init__(self, dataset, chart, feature=None, feature_ref=None, title=None, title_ref=None, description=None, description_ref=None):
        self.data = pd.DataFrame()
        self.RefDataset = dataset

        # self.chart = chart
        self.chart_type = None
        self.set_chart_type(get_function_stack())

        self.feature = Feature(feature, feature_ref)
        self.title = Title(title, title_ref)
        self.description = Description(description, description_ref)

        self.preprocess = DtPreprocess(dataset)
        self.preprocess.validate()

        self. build()

    def build(self):
        if not validate_dataset(self.RefDataset):
            raise ValueError("Received a dataset with basic norms of equal size and got an dataset with improper data values. please refer the docs for a proper set of dataset values.")


    def set_chart_type(self, chart):
        with open("charts.json", 'r') as file:
            data = json.load(file)

            for key in data:
                charts = data[key]
                if self.chart in charts:
                    self.chart_type = key
                    break
        if self.chart_type is None:
            raise NotImplementedError(f"The method ({self.chart}) you are attempting to use is not completely implemented yet "
                                      "and will be available in future releases. Please refer to the documentation for "
                                      "updates on its availability and usage details.")

    def get_data_modal(self):
        # improve modals here
        if self.chart == "props":
            return Prop(self.preprocess.getDtype(), self.RefDataset, self.feature, self.title, self.description)
        else:
            raise ValueError("Improper chart value.")
