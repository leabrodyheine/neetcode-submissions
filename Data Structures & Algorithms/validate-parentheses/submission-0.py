class Solution:
    def isValid(self, s: str) -> bool:
        isValidMap = {
            ')' : '(',
            '}' : '{',
            ']' : '['
        }
        stack = []

        for c in s:
            if c not in isValidMap:
                stack.append(c)
            elif stack and stack[-1] == isValidMap[c]:
                stack.pop()
            else:
                return False
            
        return not stack
            

        
