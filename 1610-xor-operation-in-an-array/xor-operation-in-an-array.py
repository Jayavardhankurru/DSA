class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        arr = [0] * n
        for i in range(n):
            arr[i] = start + (2 * i)
        xor = 0
        for num in arr:
            xor = xor ^ num
        return xor