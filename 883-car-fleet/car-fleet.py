class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        x = [(p, s) for p, s in zip(position, speed)]
        stack = []
        x.sort(reverse = True)
        for p, s in x:
            stack.append((target - p) / s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)