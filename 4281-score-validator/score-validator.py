class Solution:
    def scoreValidator(self, events: list[str]) -> list[int]:
        score = 0
        counter = 0
        i = 0
        while i < len(events) and counter < 10:
            if events[i] in "0123456":
                score += int(events[i])
            elif events[i] == "W":
                counter += 1
            elif events[i] == "WD":
                score += 1
            else:
                score += 1
            i += 1
        return [score, counter]