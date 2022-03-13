# DicomTagFinder
Simple tool to search DICOM tags.

# Dependencies
 * Python 3.8+
 * pipenv
 * pydicom
 * black
 * pytest
 
# Run dicomtagfinder
To run the dicomtagfinder follow the steps
 * Clone this repository
 * pipenv install
 * pipenv shell
 * cd src
 * python dicomtagfinder.py

# Usage examples

To display all tags

`python dicoomtagfinder -i data/0002.DCM`

Search specific tag

`python dicoomtagfinder -i data/0002.DCM -t 0008,0002 `

# Run tests

To execute test run the following command

`python -m pytest `
