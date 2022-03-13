# Util functions
import re


def dicom_tag_validator(arg_value):
    pat = re.compile(r"\b[0-9A-Fa-f]{4},[0-9A-Fa-f]{4}\b")
    if not pat.match(arg_value):
        print(
            "ERROR: Tag should be follow the format - group number,element number | E.g - 0008,0016\n"
        )
        raise ValueError
    return arg_value
