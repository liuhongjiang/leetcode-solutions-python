# The trick is not read the requirement, and consider all possible input by yourself.


class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        max_int = 2147483647
        min_int = -2147483648

        length = len(str)
        if length == 0:
            return 0

        index = 0
        while str[index] == '\t' or str[index] == ' ':
            index += 1

        sign = 1
        if str[index] == '-':
            sign = -1
            index += 1
        elif str[index] == '+':
            sign = 1
            index += 1

        num = 0
        max_len = index + 11
        while index < length and index < max_len:
            char = str[index]
            if '0' <= char <= '9':
                num = num * 10 + int(char)
            else:
                break
            index += 1
        num *= sign
        if num > max_int:
            return max_int
        elif num < min_int:
            return min_int
        else:
            return num


if __name__ == '__main__':
    solution = Solution()
    print solution.myAtoi('12345')
    print solution.myAtoi('+012345')
    print solution.myAtoi('-012345')
    print solution.myAtoi('+01a2345')
    print solution.myAtoi('+a01a2345')
    print solution.myAtoi("    010")
    print solution.myAtoi("2147483648")
    print solution.myAtoi("-2147483648")
