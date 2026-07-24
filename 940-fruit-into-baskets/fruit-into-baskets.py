class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        mpp = defaultdict(int)
        cnt = 0
        i = 0
        for j in range(len(fruits)):
            mpp[fruits[j]] += 1
            cnt += 1
            if len(mpp) > 2:
                mpp[fruits[i]] -= 1
                if mpp[fruits[i]] == 0:
                    mpp.pop(fruits[i])
                cnt -= 1
                i += 1
        return cnt