import unittest
from circle import area, perimeter
import math

class TestCircle(unittest.TestCase):
    def test_area(self):
        radius = 1
        result = area(radius)
        self.assertAlmostEqual(result, math.pi, places=7)

    def test_area_zero(self):
        radius = 0
        result = area(radius)
        self.assertEqual(result, 0)
    
    def test_perimeter(self):
        radius = 1
        result = perimeter(radius)
        self.assertAlmostEqual(result, 2 * math.pi, places=7)

    def test_perimeter_zero(self):
        radius = 0
        result = perimeter(radius)
        self.assertAlmostEqual(result, 0)

if __name__ == '__main__':
    unittest.main()