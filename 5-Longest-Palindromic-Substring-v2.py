class Solution(object):
    def findPalindrome(self, s, start, end, longest_len):
        if end - start < longest_len:
            try:
                if s[longest_len/2 + (end + start)/2] != s[(start+end+1)/2-longest_len/2]:
                    return start, end
            except IndexError:
                return start, end
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
        longest_len = 0
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
            start, end = self.findPalindrome(s, start, end, longest_len)
            if longest_end - longest_start < end - start:
                longest_start, longest_end = start, end
                longest_len = longest_end - longest_start + 1
            # fast forward to the next search point
            j = i + 1
            while j < s_len and s[i] != s[j]:
                if j - i < longest_len:
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
    print "1221 is right answer\n", solution.longestPalindrome("1221")
    print "1234567890987654321 is right answer\n", solution.longestPalindrome("1234567890987654321")
    print "d1234567890987654321d is right answer\n", solution.longestPalindrome("abcd1234567890987654321dabsdfa")
    print "123454321123454321 is right answer\n", solution.longestPalindrome("BDSAF123454321123454321bfabadf")
    print "1234555555555554321 is right answer\n", solution.longestPalindrome("1234555555555554321fsfd")
    print "55555555555 is right answer\n", solution.longestPalindrome("123455555555555")
    print "121 is right answer\n", solution.longestPalindrome("fabsdfa121")
    print "22 is right answer\n", solution.longestPalindrome("fabsdfa122")
    print "a1212121212121212121212121a is right answer\n", solution.longestPalindrome("a1212121212121212121212121a")
    print "5555 is right answer\n", solution.longestPalindrome("5555")
    print "anana is right answer\n", solution.longestPalindrome("bananas")
    print "aanaanaa is right answer\n", solution.longestPalindrome("baanaanaas")
    print "very log right answer\n", solution.longestPalindrome("aaaabbbbbbbbbbccccccccccddddddddddeeeeeeeeeeffffffffffgggggggggghhhhhhhhhhiiiiiiiiiijjjjjjjjjjkkkkkkkkkkllllllllllmmmmmmmmmmnnnnnnnnnnooooooooooppppppppppqqqqqqqqqqrrrrrrrrrrssssssssssttttttttttuuuuuuuuuuvvvvvvvvvvwwwwwwwwwwxxxxxxxxxxyyyyyyyyyyzzzzzzzzzzyyyyyyyyyyxxxxxxxxxxwwwwwwwwwwvvvvvvvvvvuuuuuuuuuuttttttttttssssssssssrrrrrrrrrrqqqqqqqqqqppppppppppoooooooooonnnnnnnnnnmmmmmmmmmmllllllllllkkkkkkkkkkjjjjjjjjjjiiiiiiiiiihhhhhhhhhhggggggggggffffffffffeeeeeeeeeeddddddddddccccccccccbbbbbbbbbbaaaaaaaabbbbbbbbbbccccccccccddddddddddeeeeeeeeeeffffffffffgggggggggghhhhhhhhhhiiiiiiiiiijjjjjjjjjjkkkkkkkkkkllllllllllmmmmmmmmmmnnnnnnnnnnooooooooooppppppppppqqqqqqqqqqrrrrrrrrrrssssssssssttttttttttuuuuuuuuuuvvvvvvvvvvwwwwwwwwwwxxxxxxxxxxyyyyyyyyyyzzzzzzzzzzyyyyyyyyyyxxxxxxxxxxwwwwwwwwwwvvvvvvvvvvuuuuuuuuuuttttttttttssssssssssrrrrrrrrrrqqqqqqqqqqppppppppppoooooooooonnnnnnnnnnmmmmmmmmmmllllllllllkkkkkkkkkkjjjjjjjjjjiiiiiiiiiihhhhhhhhhhggggggggggffffffffffeeeeeeeeeeddddddddddccccccccccbbbbbbbbbbaaaa")