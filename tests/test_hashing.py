"""testing hashami hashing function"""
import unittest

from hashami import hasher as h


class TestHashing(unittest.TestCase):
    """test deatils of hashing function"""
    def test_sorting(self):
        """test sorting"""
        self.assertEqual(
            h.hash_dict({'a': 1, 'b': 2}),
            h.hash_dict({'b': 2, 'a': 1})
        )

    def test_int_hashing(self):
        """test hashing of int"""
        try:
            h.hash_dict({'a': 123123})
        except TypeError:
            self.fail("hash_dict() raised TypeError unexpectedly!")


if __name__ == '__main__':
    unittest.main()
