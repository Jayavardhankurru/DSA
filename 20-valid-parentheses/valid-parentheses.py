from queue import LifoQueue
class Solution:
    def isValid(self, s: str) -> bool:
        stack = LifoQueue()
        n = len(s)
        for i in range(n):
            if s[i] == "(" or s[i] == "[" or s[i] == "{":
                stack.put(s[i])
            else:
                if stack.empty():
                    return False
                char = stack.get()
                if s[i] == ")" and char != "(" or s[i] == "]" and char != "[" or s[i] == "}" and char != "{":
                    return False
        return stack.empty()