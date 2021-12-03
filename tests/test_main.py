import os
import ctypes
from pyvlang import VLang


def test_compile():
    VLang.make_lib("test.v", "/tmp/test-pyvlang.so")
    assert os.path.isfile("/tmp/test-pyvlang.so")
    os.remove("/tmp/test-pyvlang.so")


def test_add_int():
    VLang.make_lib("test.v")
    lib = VLang("./test.so")
    assert lib.add(1, 2) == 3


def test_from_v():
    assert VLang.from_v("./test.v").add(3, 3) == 6


def test_string():
    VLang.make_lib("test.v")
    lib = VLang("./test.so")

    lib.echo.restype = ctypes.c_char_p
    lib.echo.argtypes = [ctypes.c_char_p]
    res = lib.echo("hello world".encode())
    assert ctypes.c_char_p(res).value.decode("UTF-8") == "hello world"
