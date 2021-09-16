import unittest
from recrusive import count_nested_tuple


class TestRecrurive(unittest.TestCase):
    def test_one(self):
        test = count_nested_tuple((1, (2, 3, (4, 5), 6)))
        expected = 6
        self.assertTrue(test,expected)
    def test_two(self):
        test = count_nested_tuple((1, (2, 3, (4, 5))))
        expected = 5
        self.assertTrue(test,expected)




if __name__ == '__main__':
    unittest.main()