import unittest
from square import area, perimeter

class TestSquare(unittest.TestCase):

    def test_area(self):
        self.assertEqual(area(1), 1)
        self.assertEqual(area(2), 4)

    def test_perimeter(self):
        self.assertEqual(perimeter(1), 4)
        self.assertEqual(perimeter(2), 8)

if __name__ == '__main__':
    unittest.main()