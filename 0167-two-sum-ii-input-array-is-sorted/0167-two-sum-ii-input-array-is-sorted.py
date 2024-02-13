class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        myDict={}
        for num in numbers:
            myDict[num] = target-num
        for i in range(len(numbers)):
            if myDict[numbers[i]] in numbers:
                if numbers.index(myDict[numbers[i]]) == i:
                    continue
                return sorted([i+1, numbers.index(myDict[numbers[i]])+1])