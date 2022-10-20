"""testing hashami hashing function"""
import unittest

target = __import__("hashami.py")
hasher = target.dict_hasher


class TestHashing(unittest.TestCase):
    """test deatils of hashing function"""
    def test_sorting(self):
        """test sorting"""
        self.assertEqual(hasher({'a': 1, 'b': 2}), hasher({'b': 2, 'a': 1}))


if __name__ == '__main__':
    unittest.main()
