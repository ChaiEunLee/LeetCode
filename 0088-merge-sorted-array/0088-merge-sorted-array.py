class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        index1 = m
#        print(index1)
        for j in range(len(nums2)):
            nums1[index1] = nums2[j]
            index1 += 1
            
        nums1.sort()