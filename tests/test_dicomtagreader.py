from src.dicomtagreader import DicomTagReader


def test_get_dicom_tag_should_return_none():
    dicom_reader = DicomTagReader()
    dicom_reader.open_dicom("./data/0002.DCM")

    val = dicom_reader.get_dicom_tag("0x00010215")

    assert val == None


def test_get_dicom_meta_tag_should_return_none():
    dicom_reader = DicomTagReader()
    dicom_reader.open_dicom("./data/0002.DCM")

    val = dicom_reader.get_dicom_meta_tag("0x00010215")

    assert val == None
