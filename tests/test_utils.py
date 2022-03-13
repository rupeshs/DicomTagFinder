import pytest
from src.utils import dicom_tag_validator


def test_dicom_tag_validator_should_raise_error_for_tag_invalid_length():

    with pytest.raises(ValueError):
        dicom_tag_validator("008")


def test_dicom_tag_validator_should_raise_error_for_invalid_characters():

    with pytest.raises(ValueError):
        dicom_tag_validator("abcdrest")


def test_dicom_tag_validator_should_raise_error_seperated_by_comma():

    with pytest.raises(ValueError):
        dicom_tag_validator("0008.0016")


def test_dicom_tag_validator_should_raise_error_for_invalid_hex():

    with pytest.raises(ValueError):
        dicom_tag_validator("00GH,0016")
