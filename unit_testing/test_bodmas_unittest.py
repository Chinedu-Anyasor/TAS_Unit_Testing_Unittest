import bodmas

import unittest


class TestBodmas(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(bodmas.addition(3, 1), 4)

    def test_subtraction(self):
        self.assertEqual(bodmas.subtraction(23, 13), 10)

    def test_subtraction(self):
        self.assertEqual(bodmas.subtraction(18, 13), 4)


if __name__ == '__main__':
        unittest.main()
