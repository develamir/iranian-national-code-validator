import argparse
import sys
from typing import Optional
def clean_national_code(code: str) -> str:
    """Return only ASCII digits from the input."""
    return "".join(ch for ch in code if ch in "0123456789")
def calculate_check_digit(first_nine: str) -> Optional[int]:
    """Calculate the 10th check digit for the first 9 digits."""
    if len(first_nine) != 9 or not first_nine.isdigit():
        return None
    total = sum(int(digit) * (10 - index) for index, digit in enumerate(first_nine))
    remainder = total % 11
    if remainder < 2:
        return remainder
    return 11 - remainder
def is_valid_national_code(code: str) -> bool:
    """Validate an Iranian national code (کد ملی)."""
    digits = clean_national_code(code)
    if len(digits) != 10:
        return False
    if len(set(digits)) == 1:
        return False
    first_nine = digits[:9]
    expected = calculate_check_digit(first_nine)
    if expected is None:
        return False
    return int(digits[9]) == expected
def format_national_code(code: str) -> str:
    """Return only the digits of a national code."""
    return clean_national_code(code)
def main(argv: Optional[list[str]] = None) -> int:
    parser = argparse.ArgumentParser(description="Validate Iranian national codes (کد ملی).")
    parser.add_argument("code", nargs="?", help="National code to validate")
    parser.add_argument("--check-digit", metavar="NINE", help="Calculate check digit for 9 digits")
    args = parser.parse_args(argv)
    if args.check_digit:
        check = calculate_check_digit(args.check_digit)
        if check is None:
            print("Invalid input: provide exactly 9 digits.", file=sys.stderr)
            return 1
        print(check)
        return 0
    if not args.code:
        parser.print_help(sys.stderr)
        return 1
    digits = format_national_code(args.code)
    if is_valid_national_code(args.code):
        print(f"{digits}: valid")
        return 0
    print(f"{digits}: invalid")
    return 1
if __name__ == "__main__":
    raise SystemExit(main())
