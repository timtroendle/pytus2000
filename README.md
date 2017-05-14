# PyTUS2000

[![DOI](https://zenodo.org/badge/76587025.svg)](https://zenodo.org/badge/latestdoi/76587025)

A library for working with the [UK Time Use Survey 2000](http://doi.org/10.5255/UKDA-SN-4504-1) data.

## User Guide

`pytus2000` comes with classes for all categorial data in the UK Time Use Survey and hence provides you with metadata and tab-completion while you are working with the data set. As an example consider you want to filter out all adult diary data. Instead of a query like this:

```python
adults = diary_data[diary_data.DTYPE == 1]
```

`pytus2000` lets you write:

```python
adults = diary_data[diary_data.DTYPE == diary.DTYPE.ADULT_DIARY]
```

Start by reading in a tab-delimited data set as a pandas DataFrame like so:

```python
import pytus2000 as tus
from pytus2000 import diary

tus.set_cache_location('<path_to_cachedir>') # caches the pandas dataframe, next read will be fast
diary_data = tus.read_diary_file('<path_to_file>')
```

### Installation

#### From GitHub

`pip install git+git://github.com/timtroendle/pytus2000@master`

## Developer Guide

### Installation

Best install `pytus2000` in editable mode:

    $ pip install -e .

### Run the test suite

Make sure you have set up your environment as described above. Run the test suite with py.test:

    $ py.test

Tests including the data set are skipped by default, as the data set might be unavailable and tests are slow. To run all tests run:

    $ py.test --runwithdataset

### Auto generate the code

Most of the code is auto generated from the data dictionaries provided with the data set. Follow these steps if you want to generate the code.

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
