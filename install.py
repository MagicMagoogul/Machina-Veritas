# A quick script to install all dependencies needed to run this project.

# Import all libraries

import argparse, math, sys, json, datetime as dt
from typing import Dict, Any, List, Tuple
import pandas as pd
import numpy as np

def main():
    print(" All imports successful!")
    print(f"Pandas version: {pd.__version__}")
    print(f"Numpy version: {np.__version__}")
    print(f"Datetime now: {dt.datetime.now()}")

if __name__ == "__main__":
    main()


# If a library fails to import, please install it using pip:
# EXAMPLE -- pip install pandas numpy


# Sanity Check for data


# Looking for data to process


# Final results