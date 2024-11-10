import unittest
from math_quiz import function_A, function_B, function_C


class TestMathGame(unittest.TestCase):

    def test_function_A(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = function_A(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_function_B(self):
        # Assuming function_B performs an arithmetic calculation, e.g., multiplication
        test_cases = [
            (3, 4, 12),
            (5, 5, 25),
            (7, 8, 56),
            (0, 10, 0),  # edge case with zero
            (-1, 8, -8)  # edge case with negative numbers
        ]
        
        for num1, num2, expected_result in test_cases:
            result = function_B(num1, num2)
            self.assertEqual(result, expected_result, f"Failed on input: {num1}, {num2}")

    def test_function_C(self):
        # Test if function_C can generate a math problem and return the correct answer
        test_cases = [
            (5, 2, '+', '5 + 2', 7),
            (10, 3, '-', '10 - 3', 7),
            (4, 6, '*', '4 * 6', 24),
            (8, 2, '/', '8 / 2', 4),  # basic division case
        ]

        for num1, num2, operator, expected_problem, expected_answer in test_cases:
            problem, answer = function_C(num1, num2, operator)
            self.assertEqual(problem, expected_problem, f"Problem generation failed for {num1} {operator} {num2}")
            self.assertEqual(answer, expected_answer, f"Answer calculation failed for {num1} {operator} {num2}")

if __name__ == "__main__":
    unittest.main()
