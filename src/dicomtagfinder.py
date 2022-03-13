" DICOM tag finder "

import sys
import argparse
from utils import dicom_tag_validator
from dicomtagreader import DicomTagReader


def get_tag(tag):
    format_tag = tag.replace(",", "")
    tag_num = 0
    try:
        tag_num = int(format_tag, 16)
    except ValueError:
        print("Invalid tag format")
    return tag_num


def main():
    parser = argparse.ArgumentParser(description="DICOM Tag Finder v1.0",)

    parser.add_argument(
        "-i", "--image", help="Source DICOM path", required=True,
    )
    parser.add_argument(
        "-t",
        "--tag",
        help="DICOM tag group number,element number | E.g - 0008,0016",
        type=dicom_tag_validator,
    )

    parser.add_argument(
        "-a", "--all", action="store_true", help="Print all tags",
    )
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)
    else:
        args = parser.parse_args()

    dicom_reader = DicomTagReader()
    dicom_reader.open_dicom(str(args.image))

    if args.tag:
        tag_num = get_tag(args.tag)
        if tag_num == 0:
            sys.exit(1)

        tag_hex = hex(tag_num)
        tag_value = dicom_reader.get_dicom_tag(tag_hex)
        if not tag_value:
            tag_value = dicom_reader.get_dicom_meta_tag(tag_hex)

        if tag_value:
            print(tag_value)
        else:
            print(f"ERROR: Tag -> {args.tag} not found!")
    else:
        print(dicom_reader.dataset)


if __name__ == "__main__":
    main()
