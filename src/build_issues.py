"""Takes Issues Filed in the last week and puts them in a file for the upcoming stream"""
import pathlib
import github
from datetime import datetime

# Get the date of the next friday
