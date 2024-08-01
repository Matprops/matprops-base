import numpy as np
import inspect

def get_function_stack():
    stack = inspect.stack()

    # the called function is two levels from the current function
    caller_frame = stack[2]
    caller_name = caller_frame.function
    return caller_name

def checkNotNull(data):
    return False if data is None else True

def eval_list(data, max_size=1):
    arr = np.array(data)
    if checkNotNull(data):
        if arr.ndim > max_size:
            raise ValueError(f"Expected a list of data with the maximum dimensions of 1 row (only a list of data). But got a data with the dimension {arr.ndim}")
    else:
        raise ValueError("Expected a list of data, instead received a None object")
    return True

def eval_dict(data, max_size=1, fixed_size=1):
    if checkNotNull(data):
        if len(data) != fixed_size:
            raise ValueError(f"Expected a dictionary with 1 key and a list of data as value. But got a dict of length {len(data)}")
    else:
        raise ValueError("Expected a dict of 1 key, instead received a None object")
    return True