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
        psee = [-1] * n
        for i in range(n):
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()
            if stack:
                psee[i] = stack[-1]
            stack.append(i)
        return psee

    def sumSubarrayMins(self, arr: List[int]) -> int:
        mod = int(1e9 + 7)
        total = 0
        n = len(arr)
        nse = self.NSE(arr)
        pse = self.PSEE(arr)
        for i in range(n):
            left = i - pse[i]
            right = nse[i] - i
            total = (total + (right * left * arr[i]) % mod) % mod
        return total