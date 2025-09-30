class Solution:
    def NSE(self, arr):
        n = len(arr)
        nse = [n] * n
        stack = []
        for i in range(n-1, -1, -1):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            if stack:
                nse[i] = stack[-1]
            stack.append(i)
        return nse
    
    def PSEE(self, arr):
        n = len(arr)
        psee = [-1] * n
        stack = []
        for i in range(n):
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()
            if stack:
                psee[i] = stack[-1]
            stack.append(i)
        return psee

    def NGE(self, arr):
        n = len(arr)
        nge = [n] * n
        stack = []
        for i in range(n-1, -1, -1):
            while stack and arr[stack[-1]] <= arr[i]:
                stack.pop()
            if stack:
                nge[i] = stack[-1]
            stack.append(i)
        return nge

    def PGEE(self, arr):
        n = len(arr)
        pgee = [-1] * n
        stack = []
        for i in range(n):
            while stack and arr[stack[-1]] < arr[i]:
                stack.pop()
            if stack:
                pgee[i] = stack[-1]
            stack.append(i)
        return pgee

    def subArrayRanges(self, arr: List[int]) -> int:
        total = 0
        n = len(arr)
        nse = self.NSE(arr)
        psee = self.PSEE(arr)
        nge = self.NGE(arr)
        pgee = self.PGEE(arr)
        for i in range(n):
            left_min = i - psee[i]
            right_min = nse[i] - i
            left_max = i - pgee[i]
            right_max = nge[i] - i
            total += (left_max * right_max * arr[i]) - (left_min * right_min * arr[i]) 
        return total