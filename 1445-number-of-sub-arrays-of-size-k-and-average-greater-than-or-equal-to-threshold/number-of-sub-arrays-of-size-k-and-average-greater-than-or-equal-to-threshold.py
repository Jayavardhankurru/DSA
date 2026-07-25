class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        i = 0
        cnt = 0
        summ = 0
        for j in range(len(arr)):
            summ += arr[j]
            if j - i + 1 == k:
                average = summ / k
                if average >= threshold:
                    cnt += 1
                summ -= arr[i]
                i += 1
        return cnt
