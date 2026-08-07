class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor = 0
        for num in nums:
            xor = xor ^ num
        rightmost = xor ^ (xor & (xor - 1))
        bucket1 = 0
        bucket2 = 0
        for num in nums:
            if rightmost & num:
                bucket1 = bucket1 ^ num
            else:
                bucket2 = bucket2 ^ num
        return [bucket1, bucket2] 