" DicomTagReader class "
from pydicom import dcmread


class DicomTagReader:
    def __init__(self):
        self.dataset = None

    def open_dicom(
        self,
        image_path,
    ):
        self.dataset = dcmread(image_path)

    def get_dicom_tag(
        self,
        hex_tag,
    ):
        try:
            tag_value = self.dataset[hex_tag]
        except KeyError:
            tag_value = None
        return tag_value

    def get_dicom_meta_tag(
        self,
        hex_tag,
    ):
        try:
            tag_value = self.dataset.file_meta[hex_tag]
        except KeyError:
            tag_value = None
        return tag_value
