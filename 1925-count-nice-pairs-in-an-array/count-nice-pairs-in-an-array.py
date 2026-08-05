class Solution:
    def rev(self, num):
        rev = 0
        while num:
            digit = num % 10
            rev = rev * 10 + digit
            num //= 10
        return rev

    def countNicePairs(self, nums: List[int]) -> int:
        mpp = defaultdict(int)
        mod = 10 ** 9 + 7
        ans = 0
        for i in nums:
            val = i - self.rev(i)
            ans += mpp[val]
            mpp[val] += 1
        return ans % mod
        
