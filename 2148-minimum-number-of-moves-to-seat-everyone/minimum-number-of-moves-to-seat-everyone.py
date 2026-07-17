class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()
        i = 0
        total = 0
        while i < len(seats):
            total += abs(students[i] - seats[i])
            i += 1
        return total