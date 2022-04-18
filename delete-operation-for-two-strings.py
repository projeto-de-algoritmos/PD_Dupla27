class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        @cache
        def recursion(i1, i2):
            if i1 == len(word1):
                return len(word2) - i2

            if i2 == len(word2): 
                return len(word1) - i1

            not_take1 = not_take2 = take = float('infinity')
            if word1[i1] != word2[i2]:
                not_take1 = recursion(i1+1, i2) + 1
                not_take2 = recursion(i1, i2+1) + 1
            else:
                take = recursion(i1+1, i2+1)

            return min(take, not_take1, not_take2)

        return recursion(0, 0)