class Solution:
    def longestPalindrome(self, s: str) -> str:
        

        def dp(l, r):
            if l >= 0 and r <= len(s) - 1 and s[l] == s[r]:
                return dp(l-1, r+1)
            return s[l+1:r]
        
        best = ""
        for i in range(len(s)):
            best = max(best, dp(i, i), dp(i, i+1), key=len)
        return best