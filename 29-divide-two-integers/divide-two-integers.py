class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        if dividend == divisor:
            return 1
        sign = True
        if dividend > 0 and divisor < 0:
            sign = False
        elif dividend < 0 and divisor > 0:
            sign = False
        n = abs(dividend)
        d = abs(divisor)
        quotient = 0
        while n >= d:
            cnt = 0
            while n >= d << (cnt + 1):
                cnt += 1
            quotient += 1 << cnt
            n -= d << cnt
        if quotient == (1<<31) and sign:
            return INT_MAX
        if quotient == (1<<31) and not sign:
            return INT_MIN
        if sign == True:
            return quotient
        if sign == False:
            return -(quotient)