import unittest


class Solution(object):
    def __init__(self):
        self.cache = {}

    def match_one_any_char(self, s, p, s_index, p_index):
        return True, s_index + 1, p_index + 1

    def match_one_char(self, s, p, s_index, p_index):
        if s[s_index] == p[p_index]:
            return True, s_index + 1, p_index + 1
        else:
            return False, s_index, p_index

    def match_multiple_any_char(self, s, p, s_index, p_index):
        if p_index + 2 == len(p):
            return True, len(s), len(p)
        else:
            match = self.isMatch(s[s_index:], p[p_index + 2:])
            self.cache[s[s_index:] + p[p_index + 2:]] = match
            if match:
                return True, len(s), len(p)
            else:
                match = self.isMatch(s[s_index + 1:], p[p_index:])
                self.cache[s[s_index + 1:] + p[p_index:]] = match
                if match:
                    return True, len(s), len(p)
                else:
                    return False, s_index, p_index

    def match_multiple_char(self, s, p, s_index, p_index):
        match = self.isMatch(s[s_index:], p[p_index + 2:])
        self.cache[s[s_index:] + p[p_index + 2:]] = match
        if match:
            return True, len(s), len(p)
        elif s[s_index] == p[p_index]:
            match = self.isMatch(s[s_index + 1:], p[p_index:])
            self.cache[s[s_index + 1:] + p[p_index + 2:]] = match
            if match:
                return True, len(s), len(p)
            else:
                return False, s_index, p_index
        else:
            return False, s_index, p_index

    def match_next(self, s, p, s_index, p_index):
        if p_index < len(p) - 1 and p[p_index + 1] == "*":
            if p[p_index] == ".":
                return self.match_multiple_any_char(s, p, s_index, p_index)
            else:
                return self.match_multiple_char(s, p, s_index, p_index)
        else:
            if p[p_index] == ".":
                return self.match_one_any_char(s, p, s_index, p_index)
            else:
                return self.match_one_char(s, p, s_index, p_index)

    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        cached = self.cache.get(s + p, None)
        if cached is not None:
            return cached
        if len(p) == len(s) == 0:
            return True
        s_index = 0
        p_index = 0

        while s_index != len(s) and p_index != len(p):
            match, s_index, p_index = self.match_next(s, p, s_index, p_index)
            if not match:
                return False

        while p_index < len(p) - 1 and p[p_index + 1] == '*':
            p_index += 2

        if s_index == len(s) and p_index == len(p):
            return True
        else:
            return False


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def tearDown(self):
        pass

    def testIsMatch(self):
        test_pairs = [
            ("aa", "a", False),
            ("aa", "aa", True),
            ("aaa", "aa", False),
            ("aa", "a*", True),
            ("aa", ".*", True),
            ("ab", ".*", True),
            ("aab", "c*a*b", True),
            ("", "", True),
            ("123abc", "123.*abc", True),
            ("123abcabc", "123.*abc", True),
            ("123abcabcabcabc", "123.*abc", True),
            ("aaaaaaa", "a*aa", True),
            ("aa", "a*aa", True),
            ("aa", "a*.*", True),
            ("aa", "a*c*", True),
            ("", "a*b*", True),
            ("aaaaaaaaaaaaab", "a*a*a*a*a*a*a*a*a*a*c", False),
            ("acaabbaccbbacaabbbb", "a*.*b*.*a*aa*a*", False),
            ("aa", "a*c*a", True),
            ("aaa", "ab*a*c*a", True),
            ("ab", ".*..", True),
            ("ab", ".*ab.*", True),
            ("abcac", ".*ab.a.*a*", True),
            ("abcaaaaaaabaabcabac", ".*ab.a.*a*a*.*b*b*", True),
            ("abbaaaabaabbcba", "a*.*ba.*c*..a*.a*.", True)
        ]
        for pair in test_pairs:
            self.assertEqual(self.solution.isMatch(pair[0], pair[1]), pair[2])
            self.solution.cache = {}


if __name__ == "__main__":
    unittest.main()
    pass
