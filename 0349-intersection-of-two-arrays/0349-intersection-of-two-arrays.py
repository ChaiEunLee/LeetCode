class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # 짧은 쪽하나 정하고 그걸 다른쪽에서 찾는걸로
        def search(setlist, target, answer):
            #print(setlist, target)
            if len(setlist)==0:
                return
            mid = len(setlist)//2
            if setlist[mid]==target:
                answer.append(target)
                return target
            elif setlist[mid]>target:
                #print("tmp ",setlist, mid, setlist[0:mid])
                search(setlist[0:mid], target, answer)
            else:
                search(setlist[mid+1:], target, answer)
        
        set1 = set(nums1)
        set2 = set(nums2)
        answer = []
        if len(set1)>len(set2):
            for element in set2:
                search(sorted(set1), element, answer)
        else:
            for element in set1:
                search(sorted(set2), element, answer)
        return answer