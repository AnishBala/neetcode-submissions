class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max = arr[-1]
        for num in range(len(arr) - 1, -1, -1):
            if arr[num] < max:
                arr[num] = max
            else:
                temp = arr[num]
                arr[num] = max
                max = temp
        arr[-1] = -1
        return arr