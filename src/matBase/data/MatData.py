from ..utils.common import get_function_stack, get_chart_type, get_dtype, checkNotNull
from components import ChartDataFactory

class MatData:
    def __init__(self, data, **kwargs):
        self.chart = get_function_stack()
        self.chart_type = get_chart_type(self.chart)

        self.raw_data = data
        self.data_t = None

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
            modal = factory.process_data(self.chart_type, self.raw_data, self.data_t, **kwargs)

