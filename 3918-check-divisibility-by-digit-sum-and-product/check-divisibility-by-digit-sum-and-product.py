class Solution:
    def checkDivisibility(self, n: int) -> bool:
        dig_sum = 0
        temp_n = n
        dig_product = 1
        if n == 0:
            return False
        while temp_n > 0:
            digit = temp_n % 10
            dig_sum += digit
            dig_product *= digit
            temp_n //= 10
        total_sum = dig_sum + dig_product
        if n % total_sum == 0:
            return True
        else:
            return False