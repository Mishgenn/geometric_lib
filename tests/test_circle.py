import unittest
from circle import area, perimeter
import math

class TestCircle(unittest.TestCase):

    def test_area(self):
        self.assertAlmostEqual(area(1), math.pi)
        self.assertAlmostEqual(area(2), 4 * math.pi)

    def test_perimeter(self):
        self.assertAlmostEqual(perimeter(1), 2 * math.pi)
        self.assertAlmostEqual(perimeter(2), 4 * math.pi)

if __name__ == '__main__':
    unittest.main()