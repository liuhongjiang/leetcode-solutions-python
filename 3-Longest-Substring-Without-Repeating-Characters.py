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
            if s[i] in substring_map:
                position = substring_map[s[i]]
                length = i - start
                start = position + 1
                longest = length if length > longest else longest
                new_map = {}
                new_map.update((k, v) for k, v in substring_map.iteritems() if v > position)
                substring_map = new_map
            substring_map[s[i]] = i
        longest = len(substring_map) if len(substring_map) > longest else longest
        return longest

if __name__ == "__main__":
    solution = Solution()
    print solution.lengthOfLongestSubstring("bbbbbb")
    print solution.lengthOfLongestSubstring("abcabcbb")
    print solution.lengthOfLongestSubstring("abcabcbb1234567")
    print solution.lengthOfLongestSubstring("cdd")
    print solution.lengthOfLongestSubstring("dvdf")
