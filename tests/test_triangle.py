import unittest
from triangle import area, perimeter

class TestTriangle(unittest.TestCase):

    def test_area(self):
        self.assertAlmostEqual(area(3, 4, 5), 6.0)
        self.assertAlmostEqual(area(5, 5, 5), 10.825317547305486)

    def test_perimeter(self):
        self.assertEqual(perimeter(3, 4, 5), 12)
        self.assertEqual(perimeter(5, 5, 5), 15)

if __name__ == '__main__':
    unittest.main()