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

    def maximumPrimeDifference(self, nums: List[int]) -> int:
        ans = 0
        i = 0
        j  = len(nums) - 1
        while i <= j:
            if self.isPrime(nums[i]) and self.isPrime(nums[j]):
                ans = abs(j - i)
                break
            elif self.isPrime(nums[i]) and not self.isPrime(nums[j]):
                j -= 1
            elif not self.isPrime(nums[i]) and self.isPrime(nums[j]):
                i += 1
            else:
                i += 1
                j -= 1
        return ans