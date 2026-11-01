from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        dq = deque()
        dict = {')': '(', ']' : '[', '}' : '{'}
        for i in s:
            if i in ['(', '{', '[']:
                dq.append(i)
            else:
                if not dq: return False
                c = dq.pop()
                if c != dict[i]: return False
        if dq: return False
        return True