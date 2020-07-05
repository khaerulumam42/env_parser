import pytest
import os
from utils.parser import dot_env

outfile = "env.example.test"
dot_env(outfile, ".env")

def test_exist_file():
    list_dir = os.listdir(os.getcwd())
    assert outfile in list_dir, "file doesn't exists"

def test_result():
    with open("env.example", "r") as f:
        result_standard = f.readlines()
    
    with open("env.example.test", "r") as f:
        result_test = f.readlines()
    
    assert result_standard == result_test, "result not same"

