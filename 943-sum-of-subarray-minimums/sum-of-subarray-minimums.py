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

    def sumSubarrayMins(self, arr: List[int]) -> int:
        total  = 0
        n = len(arr)
        mod = int(1e9 + 7)
        nse = self.NSE(arr)
        psee = self.PSEE(arr)
        for i in range(n):
            left = i - psee[i]
            right = nse[i] - i
            total = (total + (right * left * arr[i]) % mod) % mod
        return total