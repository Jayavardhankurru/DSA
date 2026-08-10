class Solution:
    def isPrime(self, num):
        if num < 2:
            return False
        if num == 2:
            return True
        if num % 2 == 0:
            return False
        for i in range(3, int(num ** 0.5) + 1, 2):
            if num % i == 0:
                return False
        return True

    def sumFourDivisors(self, nums: List[int]) -> int:
        total = 0
        for num in nums:
            p = round(num ** (1 / 3))
            if p ** 3 == num and self.isPrime(p):
                total += 1 + p + p * p + num
                continue
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    j = num // i
                    if i != j and self.isPrime(i) and self.isPrime(j):
                        total += 1 + i + j + num
        return total