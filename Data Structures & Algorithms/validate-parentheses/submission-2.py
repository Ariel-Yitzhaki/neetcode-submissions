class Solution:
    def isValid(self, s: str) -> bool:
        stack = []        
        mapin = {'(', '{', '['}
        
        
        for i in range(len(s)):
            if s[i] in mapin:
                stack.append(s[i])
            else:
                if not stack:
                    return False
                if s[i] == ')' and stack[-1] == '(':
                    stack.pop()
                elif s[i] == '}' and stack[-1] == '{':
                    stack.pop()
                elif s[i] == ']' and stack[-1] == '[':
                    stack.pop()
                else:
                    return False
        if stack:
            return False
        return True