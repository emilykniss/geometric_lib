# tests/test_circle.py

import unittest
import math
from circle import area, perimeter


class TestCircleFunctions(unittest.TestCase):

    def test_area_positive(self):
        # Arrange
        radius = 8
        expected_result = math.pi * radius**2

        # Act
        result = area(radius)

        # Assert
        self.assertEqual(result, expected_result)

    def test_area_zero(self):
        # Arrange
        radius = 0
        expected_result = 0

        # Act
        result = area(radius)

        # Assert
        self.assertEqual(result, expected_result)

    def test_area_negative(self):
        # Arrange
        radius = -8

        # Act & Assert
        with self.assertRaises(ValueError):
            area(radius)

    def test_perimeter_positive(self):
        # Arrange
        radius = 3
        expected_result = 2 * math.pi * radius

        # Act
        result = perimeter(radius)

        # Assert
        self.assertEqual(result, expected_result)

    def test_perimeter_zero(self):
        # Arrange
        radius = 0
        expected_result = 0

        # Act
        result = perimeter(radius)

        # Assert
        self.assertEqual(result, expected_result)

    def test_perimeter_negative(self):
        # Arrange
        radius = -3

        # Act & Assert
        with self.assertRaises(ValueError):
            perimeter(radius)


if __name__ == "__main__":
    unittest.main()
