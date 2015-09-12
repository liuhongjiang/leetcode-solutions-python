import math
import unittest


class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        max_int = 2147483647
        if x < 0 or x > max_int:
            return False
        if x < 10:
            return True

        base = 10 ** int(math.log(x, 10))
        while base > 0:
            if x / base == x % 10:
                x = x % base / 10
                base /= 100
            else:
                return False
        return True


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def tearDown(self):
        pass

    def testIsPalindrome(self):
        self.assertEqual(self.solution.isPalindrome(121), True)
        self.assertEqual(self.solution.isPalindrome(-121), False)
        self.assertEqual(self.solution.isPalindrome(-77), False)
        self.assertEqual(self.solution.isPalindrome(76), False)
        self.assertEqual(self.solution.isPalindrome(0), True)
        self.assertEqual(self.solution.isPalindrome(-2147447412), False)


if __name__ == "__main__":
    # unittest.main()
    pass
