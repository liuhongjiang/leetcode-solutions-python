class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        longest = 0
        substring_map = {}
        start = 0
        for i in range(len(s)):
            position = substring_map.get(s[i])
            if position is not None and position >= start:
                length = i - start
                start = position + 1
                longest = max(length, longest)
            substring_map[s[i]] = i
        longest = max(len(s) - start, longest)
        return longest

if __name__ == "__main__":
    solution = Solution()
    # print solution.lengthOfLongestSubstring("bbbbbb")
    # print solution.lengthOfLongestSubstring("abcabcbb")
    # print solution.lengthOfLongestSubstring("abcabcbb1234567")
    # print solution.lengthOfLongestSubstring("cdd")
    # print solution.lengthOfLongestSubstring("dvdf")
    print solution.lengthOfLongestSubstring("pwwkew")
