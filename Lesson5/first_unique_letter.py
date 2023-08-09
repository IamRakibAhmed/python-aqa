"""
Solve Amazon interview question:

Create a function that will take a string as an input and return the 1st unique letter of a string.
“Google” => “l”
“Amazon” => “m”

If there are no unique letters, return an empty string: “xoxoxo” => “”.
How would you test it? How would you handle edge cases?
"""

from collections import OrderedDict


def first_unique_letter(s):
    char_count = OrderedDict()

    for char in s:
        char_lower = char.lower()
        if char_lower in char_count:
            char_count[char_lower] = False
        else:
            char_count[char_lower] = True

    for char, unique in char_count.items():
        if unique:
            return char

    return ""


def main():
    test_cases = [
        # Normal Cases
        ("Google", "l"),
        ("Amazon", "m"),

        # No Unique Letter
        ("xoxoxo", ""),

        # All Unique Letters
        ("abcdef", "a"),

        # Empty String
        ("", ""),

        # Whitespace and Special Characters
        ("a b c", "a"),
        ("!!!xyz", "x"),

        # Case Sensitivity
        ("aAaA", ""),

        # Large Input
        ("a" * 10 ** 6 + "b", "b")
    ]

    for input_str, expected_output in test_cases:
        result = first_unique_letter(input_str)
        assert result == expected_output, f"Input: {input_str}, Expected: {expected_output}, Got: {result}"


if __name__ == "__main__":
    main()
