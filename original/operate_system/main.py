import sys
import os
# from cryptography import Fernet

from login import check_passward_file as mf



def main_function():
    mf.start_make_file();
    mf.check_passward();
