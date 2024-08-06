from modal import DataModal
from ...utils.common import get_dtype, get_list_ndim

class PropDataBuilder(DataModal):
    def numpy_handler(self):
        pass

    def list_handler(self):
        pass

    def dict_handler(self):
        pass

    def dataframe_handler(self):
        pass

    def series_handler(self):
        self.data = self.raw_data.tolist()
        match self.p_name_dtype:
            case "ndarray":
                self.p_name.


        self.nlen = len(self.data)
        if self.p_name != 1:
        if self.ndim



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

    def validate_data(self):
        pass

    def __init__(self, dtype, raw_data, **kwargs):
        self.raw_data = raw_data
        self.dtype = dtype

        self.data = None
        self.nlen = None

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

