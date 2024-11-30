import unittest
from calculate import calc

class TestCalculate(unittest.TestCase):

    def test_circle_area(self):
        result = calc('circle', 'area', [1])
        self.assertAlmostEqual(result, 3.141592653589793)

    def test_circle_perimeter(self):
        result = calc('circle', 'perimeter', [1])
        self.assertAlmostEqual(result, 6.283185307179586)

    def test_square_area(self):
        result = calc('square', 'area', [2])
        self.assertEqual(result, 4)

    def test_square_perimeter(self):
        result = calc('square', 'perimeter', [2])
        self.assertEqual(result, 8)

    def test_triangle_area(self):
        result = calc('triangle', 'area', [3, 4, 5])
        self.assertAlmostEqual(result, 6.0)

    def test_triangle_perimeter(self):
        result = calc('triangle', 'perimeter', [3, 4, 5])
        self.assertEqual(result, 12)

    def test_invalid_figure(self):
        with self.assertRaises(AssertionError):
            calc('hexagon', 'area', [1])

    def test_invalid_function(self):
        with self.assertRaises(AssertionError):
            calc('circle', 'volume', [1])

    def test_invalid_triangle_sides(self):
        with self.assertRaises(AssertionError):
            calc('triangle', 'area', [1, 2, 3])  # Invalid triangle

if __name__ == '__main__':
    unittest.main()