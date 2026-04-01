class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        dic = {'+', '-', '/', '*'}
        prev, curr = 0, 0
       
        for i in range(len(tokens)):
            if len(tokens[i]) == 1 and tokens[i] in dic:
                c = tokens[i]
                curr = stack.pop()
                prev = stack.pop()
                if c == '+':
                    prev += curr
                if c == '-':
                    prev -= curr
                if c == '/':
                    prev = int(prev / curr)
                if c == '*':
                    prev *= curr
                stack.append(prev)
            else:
                stack.append(int(tokens[i]))
            
        return stack[0]


            
                