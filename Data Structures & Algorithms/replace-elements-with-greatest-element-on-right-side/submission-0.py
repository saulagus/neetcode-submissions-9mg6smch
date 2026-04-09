class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        a = []
        temp = arr[:]
        while len(a) < (len(arr)):
            temp.pop(0)
            if temp:
                maxV = max(temp)
                a.append(maxV)
            else: a.append(-1)
        return a
