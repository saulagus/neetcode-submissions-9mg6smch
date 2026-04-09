class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        maxV = -1
        for i in range(len(arr)- 1, -1,-1):
            newMax = max(maxV, arr[i])
            arr[i] = maxV
            maxV = newMax
        return arr
