import unittest
from math_quiz import generate_rand_int, generate_rand_operator, operation


class TestMathGame(unittest.TestCase):

    def test_generate_rand_int(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = generate_rand_int(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_generate_rand_operator(self):
        # Test if the generated operator is one of '+', '-', or '*'
        operators = {'+', '-', '*'}
        for _ in range(1000):  # Test a large number of random values
            rand_operator = generate_rand_operator()
            self.assertTrue(rand_operator in operators)
        

    def test_operation(self):
        test_cases = [
            (5, 2, '+', '5 + 2', 7),
            (10, 3, '-', '10 - 3', 7),
            (4, 6, '*', '4 * 6', 24),
        ]

        for num1, num2, operator, expected_problem, expected_answer in test_cases:
            problem, answer = operation(num1, num2, operator)
            self.assertEqual(problem, expected_problem)
            self.assertEqual(answer, expected_answer)

if __name__ == "__main__":
    unittest.main()
