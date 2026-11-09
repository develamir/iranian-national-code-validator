# National Code Validator
Validate Iranian national codes (کد ملی) using the official check-digit algorithm.
## Usage
python main.py 1234567891
python main.py --check-digit 123456789
## Functions
- is_valid_national_code(code): Return True if the national code is valid.
- calculate_check_digit(nine_digits): Return the 10th check digit for 9 digits.
- clean_national_code(code): Return only ASCII digits from the input.
- format_national_code(code): Return only digits from the input.
## Requirements
Python 3.11. Standard library only. No installation needed.
