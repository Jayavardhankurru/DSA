class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s1 = []
        t1 = []
        for i in s:
            if i != '#':
                s1.append(i)
            else:
                if s1:
                    s1.pop()
        for i in t:
            if i != '#':
                t1.append(i)
            else:
                if t1:
                    t1.pop()
        return "".join(s1) == "".join(t1)