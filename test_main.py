from mylib.query import create
from mylib.query import read
from mylib.query import update
from mylib.query import delete


def test_create():
    assert create() == "Success"


def test_read():
    assert read() == "Success"


def test_update():
    assert update() == "Success"


def test_delete():
    assert delete() == "Success"
