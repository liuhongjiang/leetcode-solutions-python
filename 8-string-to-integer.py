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

        while str[0] == '\t' or str[0] == ' ':
            str = str[1:]

        sign = 1
        if str[0] == '-':
            sign = -1
            str = str[1:]
        elif str[0] == '+':
            sign = 1
            str = str[1:]

        num = 0
        for char in str:
            if char >= '0' and char <= '9':
                num = num * 10 + int(char)
                if num * sign > max_int:
                    return max_int
                if num * sign < min_int:
                    return min_int
            else:
                break
        return num * sign


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
