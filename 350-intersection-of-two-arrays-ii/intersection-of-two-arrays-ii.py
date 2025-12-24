class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        freq_map = Counter(nums1)
        result = []
        for num in nums2:
            if freq_map[num] > 0:
                result.append(num)
                freq_map[num] -= 1
        return result