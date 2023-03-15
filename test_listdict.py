import unittest
from listdict import ListDictionary

class TestListDictionary(unittest.TestCase):
    def test_insert(self):
        ldict = ListDictionary()
        # insert() should return false if not
        # overwriting a key
        assert not ldict.insert(1, "hello")

    def test_remove(self):
        ldict = ListDictionary()
        ldict.insert(1, "hello")
        ldict.insert(2, "world")
        ldict.insert(3, "lorem")

        assert not ldict.remove(5)
        assert ldict.remove(2)
        assert ldict.remove(3)
        assert ldict.remove(1)

    def test_contains(self):
        ldict = ListDictionary()
        ldict.insert(1, "hello")
        ldict.insert(2, "world")
        ldict.insert(3, "lorem")

        assert ldict.contains(2)
        assert not ldict.contains(4)
        ldict.remove(2)
        assert not ldict.contains(2)

    def test_lookup(self):
        ldict = ListDictionary()
        ldict.insert(1, "hello")
        ldict.insert(2, "world")
        ldict.insert(3, "lorem")

        assert ldict.lookup(1) == "hello"
        assert ldict.lookup(2) == "world"
        assert ldict.lookup(3) == "lorem"
        assert ldict.lookup(4) == None

    def test_keys(self):
        ldict = ListDictionary()
        ldict.insert(1, "hello")
        ldict.insert(2, "world")
        ldict.insert(3, "lorem")

        keys = ldict.get_keys()
        for k in [1, 2, 3]:
            assert k in keys

    def test_values(self):
        ldict = ListDictionary()
        ldict.insert(1, "hello")
        ldict.insert(2, "world")
        ldict.insert(3, "lorem")

        values = ldict.get_values()
        for v in ["hello", "world", "lorem"]:
            assert v in values

    def test_size(self):
        ldict = ListDictionary()
        assert ldict.size() == 0
        ldict.insert(1, "hello")
        ldict.insert(2, "world")
        ldict.insert(3, "lorem")

        assert ldict.size() == 3
        ldict.remove(2)
        assert ldict.size() == 2
