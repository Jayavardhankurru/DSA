class Solution:
    def NSE(self, arr):
        n = len(arr)
        stack = []
        nse = [n] * n
        for i in range(n-1, -1, -1):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            if stack:
                nse[i] = stack[-1]
            stack.append(i)
        return nse
    
    def PSEE(self, arr):
        n = len(arr)
        stack = []
        pse = [-1] * n
        for i in range(n):
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()
            if stack:
                pse[i] = stack[-1]
            stack.append(i)
        return pse

    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        maxi = 0
        nse = self.NSE(heights)
        pse = self.PSEE(heights)
        for i in range(n):
            maxi = max(maxi, heights[i] * (nse[i] - pse[i] - 1))
        return maxi