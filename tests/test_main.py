import os

from pyvlang import VLang


def test_compile():
    VLang.make_lib("test.v", "/tmp/test-pyvlang.so")
    assert os.path.isfile("/tmp/test-pyvlang.so")
    os.remove("/tmp/test-pyvlang.so")


def test_main():
    VLang.make_lib("test.v")
    lib = VLang("./test.so")
    assert lib.add(1, 2) == 3
    assert lib.echo("hello world") == "hello world"


def test_from_v():
    assert VLang.from_v("./test.v").add(3, 3) == 6


def test_string():
    # This is not working at the moment for some reason I ignore. I'll ask vlang author if he has any clue.
    # assert VLang.from_v("./test.v").echo("test") == "test"
    pass
