#!/usr/bin/env python
#.
import sys
import numpy as np
# import pandas as pd
import flask
import sklearn

print("Python version:", sys.version)
print("NumPy version:", np.__version__)
# print("Pandas version:", pd.__version__)
print("Flask version:", flask.__version__)
print("scikit-learn version:", sklearn.__version__)

try:
    import gunicorn
    print("Gunicorn version:", gunicorn.__version__)
except ImportError:
    print("Gunicorn is not installed or cannot be imported.")
