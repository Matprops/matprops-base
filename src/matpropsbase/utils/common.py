import inspect
import json
from .defaults import CHARTS, DATARULES

def checkNotNull(data):
    return True if data is not None else False

def get_function_stack():
    stack = inspect.stack()

    # the called function is two levels from the current function
    caller_frame = stack[2]
    caller_name = caller_frame.function
    caller_name = caller_frame.function
    return caller_name

def get_chart_type(chart):
    list_charts = None
    for key in CHARTS:
        list_charts = CHARTS[key]
        if chart in list_charts:
            return key
    raise NotImplementedError(f"The method ({list_charts}) you are attempting to use is not completely implemented yet "
                              "and will be available in future releases. Please refer to the documentation for "
                              "updates on its availability and usage details.")


def get_dtype(d, param_type=None, param_name=None):
    dtype = type(d).__name__
    if param_type in DATARULES["valid_dtypes"]:
        valid_dtypes = DATARULES["valid_dtypes"][param_type]
        if dtype not in valid_dtypes:
            if param_name is not None:
                raise TypeError(f"Parameter '{param_name}' must be one of the types: {valid_dtypes}, but got the type '{dtype}'")
            else:
                raise TypeError(f"Invalid data type, expected {valid_dtypes}, but got type '{dtype}'")
    return dtype


def get_list_ndim(l):
    """
    Returns the number of dimensions of a nested list.

    Parameters:
    lst (list): The list whose dimensionality is to be determined.

    Returns:
    int: The number of dimensions of the list.
    """
    return 1 + max(get_list_ndim(item) if isinstance(item, list) for item in l)

def get_dict_ndim(d):
    return len(d)

def ndarray_to_list(data):
    pass

