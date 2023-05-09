def file_extension(filename: str):
    if '.' in filename:
        return filename.rsplit('.', 1)[1].lower()
    else:
        raise Exception("No extension")  