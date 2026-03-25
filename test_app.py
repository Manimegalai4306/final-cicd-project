from nose.tools import assert_equal
from app import add

def test_add():
    assert_equal(add(2, 3), 5)
