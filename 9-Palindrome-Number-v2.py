# An improved version of solution
# The previous solution has 5 division during each iteration
# But this version only have 2 division and 1 multiplication during each iteration
# So this version have 20% improvement of performance.

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
        reverse = 0
        current = x
        while current > 0:
            reverse = reverse * 10 + current % 10
            current /= 10
        return reverse == x


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
