class Solution(object):
    def __init__(self):
        self.cache = {}

    def _match_one_any_char(self, s, p, s_index, p_index):
        return True, s_index + 1, p_index + 1

    def _match_one_char(self, s, p, s_index, p_index):
        if s[s_index] == p[p_index]:
            return True, s_index + 1, p_index + 1
        else:
            return False, s_index, p_index

    def _match_multiple_any_char(self, s, p, s_index, p_index):
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

    def _match_multiple_char(self, s, p, s_index, p_index):
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

    def _match_next(self, s, p, s_index, p_index):
        if p_index < len(p) - 1 and p[p_index + 1] == "*":
            if p[p_index] == ".":
                return self._match_multiple_any_char(s, p, s_index, p_index)
            else:
                return self._match_multiple_char(s, p, s_index, p_index)
        else:
            if p[p_index] == ".":
                return self._match_one_any_char(s, p, s_index, p_index)
            else:
                return self._match_one_char(s, p, s_index, p_index)

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
            match, s_index, p_index = self._match_next(s, p, s_index, p_index)
            if not match:
                return False

        while p_index < len(p) - 1 and p[p_index + 1] == '*':
            p_index += 2

        if s_index == len(s) and p_index == len(p):
            return True
        else:
            return False
