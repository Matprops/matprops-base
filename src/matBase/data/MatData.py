from ..utils.common import get_function_stack, get_chart_type, get_dtype, checkNotNull
from components import ChartDataFactory

class MatData:
    def __init__(self, data, **kwargs):
        self.chart = get_function_stack()
        self.chart_type = get_chart_type(self.chart)

        self.raw_data = data
        self.data_t = None

        self.data = None
        self.prop_titles = None
        self.prop_descriptions = None

        self.len = 0

        self.validate()
        self.build(**kwargs)

    def validate(self):
        # Nullity check
        if not checkNotNull(self.raw_data):
            raise ValueError("The parameter 'data' cannot be None.")

        self.data_t = get_dtype(self.raw_data, param_type="data")

    def build(self, **kwargs):
        factory = ChartDataFactory()
        if self.data_t is not None:
            d = factory.process_data(self.chart_type, self.raw_data, self.data_t, **kwargs)
            if d.data is not None:
                self.data = d.data
            if d.p_name is not None:
                self.prop_titles = d.p_name
            if d.p_desc is not None:
                self.prop_descriptions = d.p_desc
            if d.data_len > 0:
                self.len = d.data_len

