class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        n=len(temperatures)
        res=[0]*n
        stack=[]
        for i in range(n):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                index=stack.pop()
                res[index] = i - index
            stack.append(i)
        return res