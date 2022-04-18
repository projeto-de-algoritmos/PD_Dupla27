class Solution(object):
    def longestPalindrome(self, s):
        table = [[False for i in range(len(s))] for j in range(len(s))]

        for k in range(len(s)):
            table[k][k] = True
        
        start = 0
        length = 1

        for k in range(len(s) - 1):
            if (s[k] == s[k+1]):
                start = k
                length = 2
                table[k][k+1] = True
        
        for k in range(2, len(s)):
            for i in range(len(s) - k):
                j = i + k
                if (table[i+1][j-1] and s[i] == s[j]):
                    table[i][j] = True
                    if (k + 1 > length):
                        start = i
                        length = k + 1
        
        return s[start : start + length]