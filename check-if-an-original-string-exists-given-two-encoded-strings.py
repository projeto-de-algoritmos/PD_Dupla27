class Solution:
    def possiblyEquals(self, s1: str, s2: str) -> bool:
        
        
        # Input: s1 = "internationalization", s2 = "i18n"
        @lru_cache(None)
        def recursion(i, j, diff):
            if i == len(s1) and j == len(s2): return diff == 0
            
            if i < len(s1) and s1[i].isdigit():
                k = i
                number = 0
                while k < len(s1) and s1[k].isdigit():
                    number = number*10 + int(s1[k])
                    k += 1
                    
                    if recursion(k, j, diff-number): return True
            
            elif j < len(s2) and s2[j].isdigit():
                k = j
                number = 0
                while k < len(s2) and s2[k].isdigit():
                    number = number*10 + int(s2[k])
                    k += 1
                    
                    if recursion(i, k, diff+number): return True
            
            elif diff == 0:
                if i < len(s1) and j < len(s2) and s1[i] == s2[j] and recursion(i+1, j+1, diff): return True
            elif diff > 0:
                if i < len(s1) and recursion(i+1, j, diff-1): return True
                
            elif diff < 0:
                if j < len(s2) and recursion(i, j+1, diff+1): return True
            
            return False
        
        return recursion(0, 0, 0)