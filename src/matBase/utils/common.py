import inspect
import json


def checkNotNull(data):
    return True if data is not None else False

def get_function_stack():
    stack = inspect.stack()

    # the called function is two levels from the current function
    caller_frame = stack[2]
    caller_name = caller_frame.function
    return caller_name

def get_chart_type(chart):
    with open("charts.json", 'r') as file:
        data = json.load(file)
        for key in data:
            charts = data[key]
            if chart in charts:
                return key
        raise NotImplementedError(f"The method ({chart}) you are attempting to use is not completely implemented yet "
                                  "and will be available in future releases. Please refer to the documentation for "
                                  "updates on its availability and usage details.")


def get_dtype(d, param_type=None, param_name=None):
    dtype = type(d).__name__
    with open("datarules.json", 'r') as file:
        data = json.load(file)
        if param_type in data["valid_dtypes"]:
            valid_dtypes = data["valid_dtypes"][param_type]
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
    return 1 + max(get_list_ndim(item) for item in l if isinstance(item, list))

def get_dict_ndim(d):
    return len(d)

def ndarray_to_list(data):
    pass

