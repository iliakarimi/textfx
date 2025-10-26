import io
import sys
import pytest
from textfx import *

def capture_output(func, *args, **kwargs):
    captured = io.StringIO()
    sys.stdout = captured
    func(*args, **kwargs)
    sys.stdout = sys.__stdout__
    return captured.getvalue()

def test_basic_effect():
    text = "Hello, TextFX!"
    output = capture_output(typeeffect, text)
    assert "Hello" in output

def test_scramble_effect():
    text = "Testing"
    output = capture_output(scrameffect, text)
    assert len(output.strip()) > 0
