class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        arr = list(s)
        for i in range(len(arr)):
            if arr[i] == '(':
                stack.append(i)
            elif arr[i] == ')':
                if stack:
                    stack.pop()
                else:
                    arr[i] = '#'
        while stack:
            arr[stack.pop()] = '#'
        ans = []
        for ch in arr:
            if ch != '#':
                ans.append(ch)
        return "".join(ans)
        