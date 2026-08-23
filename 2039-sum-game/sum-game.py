class Solution:
    def sumGame(self, num: str) -> bool:
        left = 0
        right = 0
        leftSum = 0
        rightSum = 0
        for i in range(len(num)):
            if num[i] == '?':
                if i < len(num) / 2:
                    left += 1
                else:
                    right += 1
            else:
                if i < len(num) / 2:
                    leftSum += int(num[i])
                else:
                    rightSum += int(num[i])
        total = left + right
        if  total % 2 == 1:
            return True
        LEFT = 2 * leftSum + 9 * left
        RIGHT = 2 * rightSum + 9 * right
        if LEFT == RIGHT:
            return False
        else:
            return True