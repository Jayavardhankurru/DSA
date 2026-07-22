class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        a = []
        for i in arr:
            for j in pieces:
               if i in j:
                for k in j:
                    a.append(k)
                pieces.remove(j)
                break
                                 
        if a == arr:
            return True
        else:
            return False