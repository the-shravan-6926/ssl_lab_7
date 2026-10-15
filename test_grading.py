
import unittest
from grading import calculate_grade


class TestGrading(unittest.TestCase):
    def test_grades(self):
        self.assertEqual(calculate_grade(80), "A")
        self.assertEqual(calculate_grade(60), "B")
        self.assertEqual(calculate_grade(40), "C")
        self.assertEqual(calculate_grade(39), "F")
        self.assertEqual(calculate_grade(100), "A")
        self.assertEqual(calculate_grade(0), "F")

    def test_invalid_marks(self):
        for marks in [-1, 101]:
            with self.assertRaises(ValueError):
                calculate_grade(marks)


if __name__ == "__main__":
    unittest.main()
