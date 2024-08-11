from props import PropDataBuilder

class ChartDataFactory:
    def __init__(self):
        self._factories = {
            'props': PropDataBuilder
        }

    def process_data(self, chart, raw_data, dtype, kwargs):
        if chart in self._factories:
            return self._factories[chart](raw_data=raw_data, dtype=dtype, kwargs=kwargs)
        else:
            raise ValueError(f"Unknown chart type: {chart}")
