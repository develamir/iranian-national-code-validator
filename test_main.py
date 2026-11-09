import unittest
import main
class TestNationalCode(unittest.TestCase):
    def test_clean_removes_non_digits(self):
        self.assertEqual(main.clean_national_code("123-456-7890"), "1234567890")
        self.assertEqual(main.clean_national_code(" 12 34 "), "1234")
    def test_calculate_check_digit_invalid_input(self):
        self.assertIsNone(main.calculate_check_digit("12345678"))
        self.assertIsNone(main.calculate_check_digit("1234567890"))
        self.assertIsNone(main.calculate_check_digit("abcdefghi"))
    def test_generated_code_is_valid(self):
        first_nine = "123456789"
        check = main.calculate_check_digit(first_nine)
        self.assertIsNotNone(check)
        code = first_nine + str(check)
        self.assertTrue(main.is_valid_national_code(code))
    def test_wrong_check_digit_is_invalid(self):
        first_nine = "123456789"
        check = main.calculate_check_digit(first_nine)
        wrong = "0" if check != 0 else "1"
        code = first_nine + wrong
        self.assertFalse(main.is_valid_national_code(code))
    def test_all_same_digits_invalid(self):
        self.assertFalse(main.is_valid_national_code("1111111111"))
        self.assertFalse(main.is_valid_national_code("0000000000"))
    def test_wrong_length_invalid(self):
        self.assertFalse(main.is_valid_national_code("123456789"))
        self.assertFalse(main.is_valid_national_code("12345678901"))
    def test_non_digits_invalid(self):
        self.assertFalse(main.is_valid_national_code("abcdefghij"))
    def test_format_returns_digits_only(self):
        self.assertEqual(main.format_national_code("12 34-56"), "123456")
if __name__ == "__main__":
    unittest.main()
