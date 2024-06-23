from preprocess import DtPreprocess
from modal.props import Prop
from constants import checkNotNull
from builder.feature import Feature
from builder.title import Title
from builder.description import Description


class MatData:
    def __init__(self, dataset, chart_type, feature=None, title=None, description=None):
        self.data = dict()
        self.chart_type = chart_type
        self.dataset = dataset

        self.feature = Feature(self.set_feature(feature))
        self.title = Title(self.set_title(title))
        self.description = Description(self.set_description(description))

        self.preprocess = DtPreprocess(dataset)
        self.preprocess.validate()

    def set_feature(self, feature):
        return self.validate_entities(feature)

    def set_title(self, title):
        return self.validate_entities(title)

    def set_description(self, description):
        return self.validate_entities(description)

    def get_data_modal(self):
        if self.chart_type == "prop":
            return Prop(self.preprocess.getDtype(), self.dataset, self.feature, self.title, self.description)
        else:
            raise ValueError("Improper chart value. expected chart values")
        # improve modals here

    def validate_entities(self, entity):
        try:
            if not checkNotNull(entity):
                return None
            if not isinstance(entity, str) and not isinstance(entity, list):
                raise TypeError("Expected type doesn't match the variable type. Expected builder types are "
                                f"list and string. But got the builder with the type: {type(entity)}")
            return entity
        except Exception as e:
            raise
