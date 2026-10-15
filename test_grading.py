
import unittest
from grading import calculate_grade


class TestGrading(unittest.TestCase):
    def test_boundary_values(self):
        cases = {
            39: "F",
            40: "C",
            59: "C",
            60: "B",
            79: "B",
            80: "A",
            100: "A",
        }

        for marks, expected in cases.items():
            with self.subTest(marks=marks):
                self.assertEqual(calculate_grade(marks), expected)

    def test_invalid_marks(self):
        for marks in [-1, 101]:
            with self.subTest(marks=marks):
                with self.assertRaises(ValueError):
                    calculate_grade(marks)

    def test_invalid_types(self):
        for marks in ["abc", None, True]:
            with self.subTest(marks=marks):
                with self.assertRaises(TypeError):
                    calculate_grade(marks)


if __name__ == "__main__":
    unittest.main()
