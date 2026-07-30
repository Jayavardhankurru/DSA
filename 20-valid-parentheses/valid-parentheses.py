from queue import LifoQueue
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        n = len(s)
        for i in range(n):
            if s[i] == "(" or s[i] == "[" or s[i] == "{":
                stack.append(s[i])
            else:
                if not stack:
                    return False
                char = stack.pop()
                if s[i] == ")" and char != "(" or s[i] == "]" and char != "[" or s[i] == "}" and char != "{":
                    return False
        return len(stack) == 0