import pytest

from datagen.dummy_datagen import hello_dummy

def inc(x):
    return x + 2

def test_answer():
    assert inc(3) == 5

def test_hello():
    rsp = hello_dummy()
    assert rsp == "howdy"
        