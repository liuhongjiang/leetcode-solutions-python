class Solution(object):
    def findPalindrome(self, s, start, end):
        for j in range(start):
            if end + 1 >= len(s):
                break
            if s[start - 1] == s[end + 1]:
                start -= 1
                end += 1
            else:
                break
        return start, end

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        longest_start = 0
        longest_end = 0
        i = 0
        while i < len(s):
            if i == len(s) - 1:
                break
            start = i
            if s[i] == s[i + 1]:
                end = i + 1
                while end + 1 < len(s) and s[start] == s[end + 1]:
                    end += 1
            else:
                end = i
            i = end + 1
            start, end = self.findPalindrome(s, start, end)
            if longest_end - longest_start < end - start:
                longest_start, longest_end = start, end
        return s[longest_start:longest_end + 1]


if __name__ == "__main__":
    solution = Solution()
    print solution.longestPalindrome("1234567890987654321")
    print solution.longestPalindrome("abcd1234567890987654321dabsdfa")
    print solution.longestPalindrome("BDSAF123454321123454321bfabadf")
    print solution.longestPalindrome("1234555555555554321fsfd")
    print solution.longestPalindrome("123455555555555")
    print solution.longestPalindrome("fabsdfa121")
    print solution.longestPalindrome("fabsdfa122")
    print solution.longestPalindrome("5555")