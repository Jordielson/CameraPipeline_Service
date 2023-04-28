from camerapipeline.shared.request_tools.json_encode import JsonEncode
from camerapipeline.shared.request_tools.multipart_encode import MultipartEncode
from camerapipeline.shared.request_tools.encode_factory import EncodeFactory
from camerapipeline.shared.request_tools.encode import Encode
from camerapipeline.shared.utlis.image import *
from camerapipeline.shared.utlis.config import *
from camerapipeline.shared.utlis.file import file_extension

from werkzeug.utils import secure_filename
import json
import cv2 as cv
import tempfile
from tqdm import tqdm 
import os
import sys

def check_input_content(request) -> Encode:

    encode: Encode = EncodeFactory.factory(request.headers.get('Content-Type'))

    if type(encode) is JsonEncode:
        data = encode.decode_request(request)
        if 'input' in data:
            encode.decode_request(request)
            return encode
        else:
            raise AttributeError("No frame present")
    elif type(encode) is MultipartEncode:
        if 'file' not in request.files:
            raise AttributeError("No file part")
        
        request_file = request.files['file']

        if request_file.filename == '':
            raise AttributeError("No selected file")
        
        if request_file:
            encode.data = json.loads(dict(request.form)['data'])            
            encode.add_file('file', secure_filename(request_file.filename), request_file.read())

            return encode
        else:
            raise AttributeError("Not a valid file")
    else:
        raise AttributeError("Invalid content type")

def process(request, callback, *args):

    encode: Encode = check_input_content(request=request)

    if type(encode) is JsonEncode:
        json = encode.decode_request(request)
        frame = image_decode_nparray(json['input'])
        del json['input']
        frame_out, encode.data = callback(frame, json, *args)
        encode.add_value('input', image_encode_nparray(frame_out))
        return encode.encode_data()
    elif type(encode) is MultipartEncode:
        filename, request_file = encode.find_file('file')
        data, out_file = process_file(data=encode.data, file=request_file, filename=filename, callback=callback, *args)

        encode.add_file('file', filename, out_file)
        encode.data = data

        return encode.encode_data()
        
def process_file(data: dict, file: bytes, filename: str, callback, *args) -> dict: 
        file_ext = file_extension(filename=filename)
        if file_ext in ALLOWED_IMAGE_EXTENSIONS:
            frame = image_decode_bytes(file)

            out_frame, data = callback(frame, data, *args)

            return data, image_encode_bytes(out_frame)
        elif file_ext in ALLOWED_VIDEO_EXTENSIONS: 
            return process_video(data=data, video=file, callback=callback)
        else:
            raise Exception("Not a valid file extension")

def process_video(data: dict, video: bytes, callback, *args) -> dict:
    with tempfile.NamedTemporaryFile(suffix='.mp4') as temp:
        temp.write(video)

        with tempfile.NamedTemporaryFile(suffix='.mp4',) as temp_out:
            video_stream = cv.VideoCapture(temp.name)

            if not video_stream.isOpened():
                raise Exception(f"Error opening video")

            width  = int(video_stream.get(cv.CAP_PROP_FRAME_WIDTH))
            height = int(video_stream.get(cv.CAP_PROP_FRAME_HEIGHT))
            fps = int(video_stream.get(cv.CAP_PROP_FPS))
            frames = int(video_stream.get(cv.CAP_PROP_FRAME_COUNT))

            out: cv.VideoWriter = cv.VideoWriter(temp_out.name, cv.VideoWriter_fourcc(*'MP4V'), fps, (width, height))

            out_data: dict = {'video': {}}

            data_without_video = data.copy()
            if 'video' in data_without_video:
                del data_without_video['video']

            for fnum in tqdm(range(frames)):
                success, frame = video_stream.read()
                if not success:
                    break

                input_data = {}
                if 'video' in data:
                    input_data = data['video'][str(fnum)] | data_without_video
                else:
                    input_data = data_without_video

                frame_out, out_data['video'][fnum] = callback(frame, input_data, *args)

                out.write(frame_out)

            video_stream.release()
            out.release()

            with tempfile.NamedTemporaryFile(suffix='.mp4',) as temp_out_264:
                os.system(f"ffmpeg -y -i {temp_out.name} -vcodec libx264 {temp_out_264.name}")
                return out_data, temp_out_264.file.read()