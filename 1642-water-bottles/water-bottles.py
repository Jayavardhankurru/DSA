class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        total = numBottles
        bottles = numBottles
        while bottles >= numExchange:
            new_bottles = bottles // numExchange
            total += new_bottles
            bottles = (bottles % numExchange) + new_bottles
        return total