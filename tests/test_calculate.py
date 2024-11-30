# tests/test_calculate.py

import unittest
from calculate import calc

PI = 3.141592653589793


class TestCalculateFunction(unittest.TestCase):

    def test_calc_circle_area(self):
        # Arrange
        fig = "circle"
        func = "area"
        size = [3]
        expected_result = PI * 3 * 3

        # Act
        result = calc(fig, func, size)

        # Assert
        self.assertEqual(result, expected_result)

    def test_calc_circle_perimeter(self):
        # Arrange
        fig = "circle"
        func = "perimeter"
        size = [3]
        expected_result = 2 * PI * 3

        # Act
        result = calc(fig, func, size)

        # Assert
        self.assertEqual(result, expected_result)

    def test_calc_square_area(self):
        # Arrange
        fig = "square"
        func = "area"
        size = [4]
        expected_result = 4 * 4

        # Act
        result = calc(fig, func, size)

        # Assert
        self.assertEqual(result, expected_result)

    def test_calc_square_perimeter(self):
        # Arrange
        fig = "square"
        func = "perimeter"
        size = [4]
        expected_result = 4 * 4

        # Act
        result = calc(fig, func, size)

        # Assert
        self.assertEqual(result, expected_result)

    def test_calc_triangle_area(self):
        # Arrange
        fig = "triangle"
        func = "area"
        size = [3, 4, 5]
        expected_result = (3 + 4 + 5) / 2

        # Act
        result = calc(fig, func, size)

        # Assert
        self.assertEqual(result, expected_result)

    def test_calc_triangle_perimeter(self):
        # Arrange
        fig = "triangle"
        func = "perimeter"
        size = [3, 4, 5]
        expected_result = 3 + 4 + 5

        # Act
        result = calc(fig, func, size)

        # Assert
        self.assertEqual(result, expected_result)

    # Negative tests

    def test_invalid_figure(self):
        # Arrange
        fig = "hexagon"
        func = "area"
        size = [5]

        # Act & Assert
        with self.assertRaises(ValueError) as context:
            calc(fig, func, size)
        self.assertEqual(str(context.exception), "Invalid figure 'hexagon'")

    def test_invalid_function(self):
        # Arrange
        fig = "circle"
        func = "volume"
        size = [5]

        # Act & Assert
        with self.assertRaises(ValueError) as context:
            calc(fig, func, size)
        self.assertEqual(str(context.exception), "Invalid function 'volume'")

    def test_invalid_size_count_for_circle_area(self):
        # Arrange
        fig = "circle"
        func = "area"
        size = [5, 10]

        # Act & Assert
        with self.assertRaises(ValueError) as context:
            calc(fig, func, size)
        self.assertEqual(
            str(context.exception),
            "Invalid size parameters for area of circle"
        )

    def test_invalid_size_count_for_triangle_area(self):
        # Arrange
        fig = "triangle"
        func = "area"
        size = [3, 4]

        # Act & Assert
        with self.assertRaises(ValueError) as context:
            calc(fig, func, size)
        self.assertEqual(
            str(context.exception),
            "Invalid size parameters for area of triangle"
        )


if __name__ == "__main__":
    unittest.main()
