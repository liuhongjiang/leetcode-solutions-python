import unittest


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        x_abs = abs(x)
        y = 0
        while x_abs != 0:
            y *= 10
            y += x_abs % 10
            x_abs /= 10

        y = -y if abs(x) != x else y
        max_int = 2147483647
        min_int = -2147483648
        if y > max_int or y < min_int:
            return 0
        return y


class SolutionTest(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def tearDown(self):
        pass

    def testReverseInteger(self):
        self.assertEqual(self.solution.reverse(100), 1)
        self.assertEqual(self.solution.reverse(-100), -1)
        self.assertEqual(self.solution.reverse(-123), -321)
        self.assertEqual(self.solution.reverse(45790), 9754)


if __name__ == "__main__":
    # unittest.main()
    pass
