import unittest
from listdict import ListDictionary

class TestListDictionary(unittest.TestCase):
    def test_insert(self):
        ldict = ListDictionary()
        # insert() should return false if not
        # overwriting a key
        assert not ldict.insert(1, "hello")

    # add more unit tests below
