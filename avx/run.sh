#!/bin/bash

source activate conda_python3

jupyter nbconvert --to html --execute test.ipynb --ExecutePreprocessor.timeout=-1 --ExecutePreprocessor.kernel_name=python3
