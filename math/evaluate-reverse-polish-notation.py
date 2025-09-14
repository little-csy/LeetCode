class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        for i in range(len(tokens)):
            if tokens[i] == '+' or tokens[i] == '-' or tokens[i] == '*' or tokens[i] == '/':
                num1 = int(tokens.pop())
                num2 = int(tokens.pop())
                if tokens[i] == '+':
                    tokens.append(num1 + num2)
                if tokens[i] == '-':
                    tokens.append(num1 - num2)
                if tokens[i] == '*':
                    tokens.append(num1 * num2)
                if tokens[i] == '/':
                    tokens.append(num2 / num1)
            
            else:
                tokens.append(tokens[i])
        
        return tokens.pop()