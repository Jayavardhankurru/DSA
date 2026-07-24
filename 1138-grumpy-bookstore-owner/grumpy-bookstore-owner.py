class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        i = 0
        satisfied = 0
        window = 0
        maxi = 0
        for j in range(len(grumpy)):
            if grumpy[j] == 1:
                window += customers[j]
            else:
                satisfied += customers[j]
            if j - i + 1 > minutes:
                if grumpy[i] == 1:
                    window -= customers[i]
                i += 1
            maxi = max(maxi , window)
        return satisfied +  maxi
