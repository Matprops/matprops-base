import math
import matplotlib.pyplot as plt

class PropConfig:
    def __init__(self, db, props):
        self.data = db
        self.props = props
        self.prop_rows = math.ceil(db.len / props) if db.len > props else 1

    def get_propFigure(self, width):
        if self.data.data is not None:
            return plt.figure(figsize=(width, 2 * self.prop_rows))
        raise ValueError("Unexpected error while parsing data passed as an argument")