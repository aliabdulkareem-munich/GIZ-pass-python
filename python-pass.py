#my naive approach algorithm is O(n^2), googling on literature showing MANACHER’S ALGORITHM as the efficient solution to this problem 
# with O(n) time complexity... https://arxiv.org/pdf/2003.08211.pdf

class Solution:
    @classmethod
    def expand_from_middle(cls, s,l,r):

            if s[l] != s[r] :
                return ""
                
            length = len(s)

            while True:
                if r+1 < length and l-1 >= 0 and s[r+1] == s[l-1]:
                    l = l - 1
                    r = r + 1
                else:
                    break
                
            
            return s[l:r+1]

    @staticmethod
    def longest_palindromic(s: str) -> str:

        length = len(s)
            
        if length == 1 or length == 0 or length == 2:
            return s
                
                
        maxP = ""

        
        #iterate over the characters, exapnd each one as the center of a palindrome
        #while keeping track of the longest palindrome we encountered so far.

        i = 0
        while i < (length - 1):
            #we expand once for even-length substring and once for odd-length substring
            substr1 = Solution.expand_from_middle(s,i,i+1)
            substr2 = Solution.expand_from_middle(s,i, i)
                
            maxSubStr = substr1 if (len(substr1) > len(substr2)) else substr2
            if len(maxSubStr) > len(maxP):
                maxP = maxSubStr
                
            i = i + 1
            
        return maxP
            
    
