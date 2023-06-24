def is_image_extension(_name:str) -> bool:
    accepted_formats = ['jpg','jpeg','png','gif'] #accepted format by fpdf #fpdf not longer in use
    file_format = _name.lower().split(".")[-1]

    for f in accepted_formats:
        if file_format == f:
            # define_file_type(file_format)
            return True
    return False