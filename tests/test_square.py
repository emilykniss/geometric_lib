# tests/test_square.py

import unittest
from square import area, perimeter


class TestSquareFunctions(unittest.TestCase):

    def test_area_positive(self):
        # Arrange
        side = 9
        expected_result = side**2

        # Act
        result = area(side)

        # Assert
        self.assertEqual(result, expected_result)

    def test_area_zero(self):
        # Arrange
        side = 0
        expected_result = 0

        # Act
        result = area(side)

        # Assert
        self.assertEqual(result, expected_result)

    def test_area_negative(self):
        # Arrange
        side = -9

        # Act & Assert
        with self.assertRaises(ValueError):
            area(side)

    def test_perimeter_positive(self):
        # Arrange
        side = 8
        expected_result = 4 * side

        # Act
        result = perimeter(side)

        # Assert
        self.assertEqual(result, expected_result)

    def test_perimeter_zero(self):
        # Arrange
        side = 0
        expected_result = 0

        # Act
        result = perimeter(side)

        # Assert
        self.assertEqual(result, expected_result)

    def test_perimeter_negative(self):
        # Arrange
        side = -8

        # Act & Assert
        with self.assertRaises(ValueError):
            perimeter(side)


if __name__ == "__main__":
    unittest.main()
