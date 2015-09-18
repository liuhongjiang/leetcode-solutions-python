class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""
        if len(strs) == 1:
            return strs[0]

        i = len(strs[0])
        for j in range(1, len(strs)):
            i = min(i, len(strs[j]))
            while i > 0 and strs[0][0:i] != strs[j][0:i]:
                i -= 1
            if i == 0:
                return ""
        return strs[0][0:i]
