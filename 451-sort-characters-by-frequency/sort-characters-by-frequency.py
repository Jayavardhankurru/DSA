class Solution:
    def frequencySort(self, s: str) -> str:
        mpp = defaultdict(int)
        for ch in s:
            mpp[ch] += 1
        mpp = sorted(mpp.items(), key=lambda item:item[1], reverse=True)
        ans = ""
        for ch, freq in mpp:
            ans += ch * freq
        return ans