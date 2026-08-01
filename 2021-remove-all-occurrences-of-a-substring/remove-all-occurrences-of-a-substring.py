class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        stack = []
        partLen = len(part)
        endChar = part[-1]
        for ch in s:
            stack.append(ch)
            if ch == endChar and len(stack) >= partLen:
                if "".join(stack[-partLen:]) == part:
                    del stack[-partLen:]
        return "".join(stack)