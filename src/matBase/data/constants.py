import pandas as pd
import numpy as np

validDtypes = [pd.DataFrame, np.ndarray, dict]


def checkNotNull(data):
    return True if data is not None else False
