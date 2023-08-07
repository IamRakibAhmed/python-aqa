"""
problem link: https://www.codewars.com/kata/5583090cbe83f4fd8c000051
Convert number to reversed array of digits
Given a random non-negative number, you have to return the digits of this number within an array in reverse order.

Example(Input => Output):
35231 => [1,3,2,5,3]
0 => [0]

make it as python multiple line comment
"""


class NumberConverter:
    @staticmethod
    def convert_to_reversed_array(num):
        return [int(digit) for digit in str(num)[::-1]]


def main():
    num = int(input("Enter a non-negative number: "))
    reversed_array = NumberConverter.convert_to_reversed_array(num)
    print("Reversed array of digits:", reversed_array)


if __name__ == "__main__":
    main()
