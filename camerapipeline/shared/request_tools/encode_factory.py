from .json_encode import *
from .multipart_encode import *
from .file_encode import *
from ..utlis.utils import check_substring_list

class EncodeFactory():

    @staticmethod
    def factory(content_type : str):
        if check_substring_list(content_type, JsonEncode.CONTENT_TYPE):
            return JsonEncode(data={})
        elif check_substring_list(content_type, MultipartEncode.CONTENT_TYPE):
            return MultipartEncode(data={})
        elif check_substring_list(content_type, FileEncode.CONTENT_TYPE):
            return FileEncode(data={})
        else:
            raise Exception("Invalid format content")

