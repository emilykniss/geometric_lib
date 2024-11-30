# tests/test_triangle.py

import unittest
from triangle import area, perimeter


class TestTriangleFunctions(unittest.TestCase):

    def test_area_positive(self):
        # Arrange
        a, b, c = 3, 4, 5
        expected_result = (a + b + c) / 2

        # Act
        result = area(a, b, c)

        # Assert
        self.assertEqual(result, expected_result)

    def test_area_negative_sides(self):
        # Arrange
        a, b, c = -3, 4, 5

        # Act & Assert
        with self.assertRaises(ValueError):
            area(a, b, c)

    def test_perimeter_positive(self):
        # Arrange
        a, b, c = 3, 4, 5
        expected_result = a + b + c

        # Act
        result = perimeter(a, b, c)

        # Assert
        self.assertEqual(result, expected_result)

    def test_perimeter_negative_sides(self):
        # Arrange
        a, b, c = -3, 4, 5

        # Act & Assert
        with self.assertRaises(ValueError):
            perimeter(a, b, c)


if __name__ == "__main__":
    unittest.main()
