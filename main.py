# This is The Major function for smFISH detection
# Starting with file I/O
# main.py
# Part 1: File input if needed
# Import anything you need for getting your file input/output)

from PyQt5.QtWidgets import QApplication
from run_Functions.run_Initial_Settings import run_init_settings  # Import the function
import sys

if __name__ == "__main__":
    run_init_settings()
