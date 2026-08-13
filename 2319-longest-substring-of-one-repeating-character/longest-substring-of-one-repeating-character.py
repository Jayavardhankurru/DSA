class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: List[int]) -> List[int]:
        n = len(s)
        tree = [0] * (4 * n)

        def build(node, start, end):
            if start == end:
                tree[node] = [s[start], s[start], 1, 1, 1, 1]
                return 
            mid = (start + end) // 2
            build(2 * node + 1, start, mid)
            build(2 * node + 2, mid + 1, end)
            tree[node] = merge(tree[2 * node + 1], tree[2 * node + 2])

        def merge(left, right):
            if left is None:
                return right
            if right is None:
                return left
            lc, lrc, llen, lpre, lsuf, lb = left
            rlc, rc, rlen, rpre, rsuf, rb = right
            length = llen + rlen
            prefix = lpre
            if lpre == llen and lrc == rlc:
                prefix = llen + rpre
            suffix = rsuf
            if rsuf == rlen and rlc == lrc:
                suffix = rlen + lsuf
            best = max(lb, rb)
            if lrc == rlc:
                best = max(best, lsuf + rpre)
            return [lc, rc, length,  prefix, suffix, best]

        def update(node, start, end, ind, char):
            if start == end:
                tree[node] = [char, char, 1, 1, 1, 1]
                return
            mid = (start + end) // 2
            if ind <= mid:
                update(2 * node + 1, start, mid, ind, char)
            else:
                update(2 * node + 2, mid + 1, end, ind, char)
            tree[node] = merge(tree[2 * node + 1], tree[2 * node + 2])
        build(0, 0, n - 1)
        ans = []
        for char, index in zip(queryCharacters, queryIndices):
            update(0, 0, n - 1, index, char)
            ans.append(tree[0][5])
        return ans