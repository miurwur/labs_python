from lab2 import find
import unittest

class TestMath(unittest.TestCase):
    def test_add_positive(self):
        self.assertEqual(find(8, [3,4,5,6,7,8,9,10,11]), (8,2))