import pandas as pd
import numpy as np

validDtypes = [pd.DataFrame, np.ndarray, dict]


def checkNotNull(data):
    return False if data is None else True


def validate_type(data, ref):
    try:
        if checkNotNull(ref) and isinstance(ref, str):
            if checkNotNull(data):
                if isinstance(data, list):
                    ent_type = "list"
                elif isinstance(data, dict):
                    ent_type = "dict"
                else:
                    raise TypeError("Expected type doesn't match the variable type. Expected data types are "
                                    f"list or dict. But got the data with the type: {type(data)}")
            else:
                ent_type = "ref"
        elif checkNotNull(ref):
            raise TypeError(f"Expected reference as string, instead got the reference as {type(ref)}")
        else:
            if checkNotNull(data):
                if isinstance(data, dict):
                    ent_type = "dict"
                else:
                    raise TypeError("There is not enough information about the name of the data that is being validated, "
                                    "Hence, we expect data to be in type of dict to use key as the feature name. "
                                    f"Instead dict, got type: {type(data)}")
            else:
                raise ValueError("Expected to receive parameters with valid types of data to validate features. Instead got None on params.")
        return ent_type
    except Exception as e:
        raise

def validate_dataset(data):
    try:
        pass
    except Exception as e:
        raise
