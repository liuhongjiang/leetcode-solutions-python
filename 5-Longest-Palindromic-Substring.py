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
        s_len = len(s)
        longest_start = 0
        longest_end = 0
        i = 0
        while i < s_len:
            if i >= s_len - (longest_end - longest_start)/2 or i >= s_len - 1:
                break
            start = i
            if s[i] == s[i + 1]:
                end = i + 1
                while end + 1 < s_len and s[start] == s[end + 1]:
                    end += 1
            else:
                end = i
            i = end
            start, end = self.findPalindrome(s, start, end)
            if longest_end - longest_start < end - start:
                longest_start, longest_end = start, end
            # fast forward to the next search point
            j = i + 1
            while j < s_len and s[i] != s[j]:
                if j - i < longest_end - longest_start:
                    j += 1
                else:
                    break
            next_i = max(i+1, (i + j)/2)
            while next_i > i+1 and s[next_i] == s[next_i - 1]:
                next_i -= 1
            i = next_i
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
    print solution.longestPalindrome("a1212121212121212121212121a")
    print solution.longestPalindrome("5555")
    print solution.longestPalindrome("bananas")
    print solution.longestPalindrome("baanaanaas")
    print solution.longestPalindrome("a")
    print solution.longestPalindrome("aaaabbbbbbbbbbccccccccccddddddddddeeeeeeeeeeffffffffffgggggggggghhhhhhhhhhiiiiiiiiiijjjjjjjjjjkkkkkkkkkkllllllllllmmmmmmmmmmnnnnnnnnnnooooooooooppppppppppqqqqqqqqqqrrrrrrrrrrssssssssssttttttttttuuuuuuuuuuvvvvvvvvvvwwwwwwwwwwxxxxxxxxxxyyyyyyyyyyzzzzzzzzzzyyyyyyyyyyxxxxxxxxxxwwwwwwwwwwvvvvvvvvvvuuuuuuuuuuttttttttttssssssssssrrrrrrrrrrqqqqqqqqqqppppppppppoooooooooonnnnnnnnnnmmmmmmmmmmllllllllllkkkkkkkkkkjjjjjjjjjjiiiiiiiiiihhhhhhhhhhggggggggggffffffffffeeeeeeeeeeddddddddddccccccccccbbbbbbbbbbaaaaaaaabbbbbbbbbbccccccccccddddddddddeeeeeeeeeeffffffffffgggggggggghhhhhhhhhhiiiiiiiiiijjjjjjjjjjkkkkkkkkkkllllllllllmmmmmmmmmmnnnnnnnnnnooooooooooppppppppppqqqqqqqqqqrrrrrrrrrrssssssssssttttttttttuuuuuuuuuuvvvvvvvvvvwwwwwwwwwwxxxxxxxxxxyyyyyyyyyyzzzzzzzzzzyyyyyyyyyyxxxxxxxxxxwwwwwwwwwwvvvvvvvvvvuuuuuuuuuuttttttttttssssssssssrrrrrrrrrrqqqqqqqqqqppppppppppoooooooooonnnnnnnnnnmmmmmmmmmmllllllllllkkkkkkkkkkjjjjjjjjjjiiiiiiiiiihhhhhhhhhhggggggggggffffffffffeeeeeeeeeeddddddddddccccccccccbbbbbbbbbbaaaa")