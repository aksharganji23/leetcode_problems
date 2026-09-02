class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack=[]
        for i in range(len(operations)):
            if operations[i]=='+':
                stack.append(int(stack[-1]+stack[-2]))
            elif operations[i]=='C':
                stack.pop()
            elif operations[i]=='D':
                stack.append(2*(stack[-1]))
            else:
                stack.append(int(operations[i]))
        return (sum(stack))
