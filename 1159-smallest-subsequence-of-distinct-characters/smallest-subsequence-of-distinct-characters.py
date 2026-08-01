class Solution:
    def smallestSubsequence(self, s: str) -> str:
        lastInd = {}
        visited = set()
        for i, ch in enumerate(s):
            lastInd[ch] = i
        stack = []
        for i, ch in enumerate(s):
            if ch in visited:
                continue
            while stack and stack[-1] > ch and lastInd[stack[-1]] > i:
                visited.remove(stack.pop())
            stack.append(ch)
            visited.add(ch)
        return "".join(stack)