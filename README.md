# PyTUS2000

A library for working with the [UK Time Use Study 2000](https://discover.ukdataservice.ac.uk/catalogue?sn=4504) data.

## Installation

### From source code

1) Download [tab delimited data set](https://discover.ukdataservice.ac.uk/catalogue?sn=4504).

2) Auto-generate the source code by running `./scripts/convert_rtf.py` and `./scripts/generate_code.py`. Help for both scripts is available through:

    python ./scripts/<script>.py --help

3) `pip install .`

## Developer Guide

### Prepare your environment

#### Download and extract data set

To run all tests and to generate the source code, you will need the original data set. Extract it into `./data/` so that it will be discovered by the test runner. Your directory should look like this:

    ./data/
        4504_file_information.rtf
        mrdoc/
            ...
        read4504.txt
        tab/
            ...
    ./pytus2000/
        ...
    ...

#### Convert rtf

The original data dictionaries come in rtf format. For running the tests and generating the source code, you will need to convert them to plain text first. Make sure you have a Python 2 environment with `pyth`, `click`, and `pathlib` installed and run:

    python ./scripts/convert_rtf.py ./data/mrdoc/allissue/ ./data/mrdoc/allissue/

#### Auto-generate data dictionaries

    python ./scripts/generate_code.py ./data/mrdoc/allissue/

You will need to repeat this step whenever you do changes to the script generating the code.

#### Install pytus

Make sure you have the source code autogenerated, see above. Best install `pytus2000` in editable mode:

    $ pip install -e .

### Run the test suite

Make sure you have set up your environment as described above. Run the test suite with py.test:

    $ py.test

Tests including the data set are skipped by default, as the data set might be unavailable and tests are slow. To run all tests run:

    $ py.test --runwithdataset
