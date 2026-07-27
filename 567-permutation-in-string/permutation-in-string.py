class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        mpp1 = [0] * 26
        mpp2 = [0] * 26
        for i in range(len(s1)):
            mpp1[ord(s1[i]) - ord('a')] += 1
        i = 0
        for j in range(len(s2)):
            mpp2[ord(s2[j]) - ord('a')] += 1
            if j - i + 1 > len(s1):
                mpp2[ord(s2[i]) - ord('a')] -= 1
                i += 1
            if j - i + 1 == len(s1):
                if mpp1 == mpp2:
                    return True
        return False