class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        greater_map = {}
        for num in nums2[::-1]:
            while stack and stack[-1] < num:
                stack.pop()
            if stack:
                greater_map[num] = stack[-1]
            stack.append(num)
        return [greater_map.get(num, -1) for num in nums1]