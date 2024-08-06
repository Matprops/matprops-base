import pandas as pd
from ...utils.common import get_dtype, get_list_ndim, verify_dimensions, get_dict_ndim

class PropDataBuilder:
    def __init__(self, raw_data, dtype, **kwargs):
        self.raw_data = raw_data
        self.dtype = dtype

        self.data = None
        self.data_ref = []

        self.p_name = None
        self.p_name_dtype = None

        self.p_desc = None
        self.p_desc_dtype = None

        self.infer_kwargs(**kwargs)
        match self.dtype:
            case "ndarray":
                self.numpy_handler()
            case "list":
                self.list_handler()
            case "dict":
                self.dict_handler()
            case "DataFrame":
                self.dataframe_handler()
            case "Series":
                self.series_handler()

    def numpy_handler(self):
        self.data = self.raw_data.tolist()
        data_len, desc_len, name_len = None, None, None

        if self.p_name_dtype == "str":
            raise ValueError("String cannot be accepted")
        elif self.p_name_dtype == "list":
            name_len = len(self.p_name)

        if self.p_desc_dtype == "str":
            raise ValueError("String cannot be accepted")
        elif self.p_desc_dtype == "list":
            desc_len = len(self.p_desc)

        if get_list_ndim(self.data) > 1:
            data_len = [len(inner_list) for inner_list in self.data]
            verify_dimensions(*data_len, name_len, desc_len)
        else:
            data_len = len(self.data)
            verify_dimensions(data_len, name_len, desc_len)
        self.validate_integrity()


    def list_handler(self):
        pass

    def dict_handler(self):
        self.data_ref, l_data = [], []
        data_len, desc_len, name_len = None, None, None
        if self.p_name_dtype == "str":
            if self.p_name in self.raw_data.keys():
                key = self.p_name
                self.p_name = self.raw_data[key]
                del self.raw_data[key]
                name_len = len(self.p_name)
            else:
                raise ValueError("Key not present in dictionary")
        elif self.p_name_dtype == "list":
            name_len = len(self.p_name)

        if self.p_desc_dtype == "str":
            if self.p_desc in self.raw_data.keys():
                key = self.p_desc
                self.p_desc = self.raw_data[key]
                del self.raw_data[key]
                desc_len = len(self.p_desc)
            else:
                raise ValueError("Key not present in dictionary")
        elif self.p_desc_dtype == "list":
            desc_len = len(self.p_desc)

        for key, value in self.raw_data.items():
            self.data_ref.append(key)
            l_data.append(value)

        if get_list_ndim(l_data) > 1:
            data_len = [len(inner_list) for inner_list in l_data]
            verify_dimensions(*data_len, name_len, desc_len)
        else:
            data_len = len(l_data)
            verify_dimensions(data_len, name_len, desc_len)
        self.validate_integrity()

    def dataframe_handler(self):
        l_data = []
        data_len, desc_len, name_len = None, None, None

        if self.p_name_dtype == "str":
            key = self.p_name
            self.p_name = self.raw_data[key].tolist()
            self.raw_data.drop(columns=[key], inplace=True)
        elif self.p_name_dtype == "list":
            name_len = len(self.p_name)

        if self.p_desc_dtype == "str":
            key = self.p_desc
            self.p_desc = self.raw_data[key].tolist()
            self.raw_data.drop(columns=[key], inplace=True)
        elif self.p_desc_dtype == "list":
            desc_len = len(self.p_desc)

        for column in self.raw_data.columns:
            self.data_ref.append(column)
            l_data.append(self.raw_data[column].tolist())

        if get_list_ndim(l_data) > 1:
            data_len = [len(inner_list) for inner_list in l_data]
            verify_dimensions(*data_len, name_len, desc_len)
        else:
            data_len = len(l_data)
            verify_dimensions(data_len, name_len, desc_len)
        self.validate_integrity()

    def series_handler(self):
        l_data = self.raw_data.tolist()
        data_len, desc_len, name_len = len(l_data), None, None

        self.data_ref = [self.raw_data.name]

        if self.p_name_dtype == "str":
            raise ValueError("String cannot be accepted")
        elif self.p_name_dtype == "list":
            name_len = len(self.p_name)

        if self.p_desc_dtype == "str":
            raise ValueError("String cannot be accepted")
        elif self.p_desc_dtype == "list":
            desc_len = len(self.p_desc)

        verify_dimensions(data_len, name_len, desc_len)
        self.validate_integrity()


    def infer_kwargs(self, **kwargs):
        """
        p_name = prop name
        p_desc = prop description
        """
        for key, value in kwargs.items():
            if key=="p_name":
                self.p_name_dtype = get_dtype(value, param_type="name")
                self.p_name = value
            elif key=="p_desc":
                self.p_desc_dtype = get_dtype(value, param_type="desc")
                self.p_desc = value

    def validate_integrity(self):
        pass
