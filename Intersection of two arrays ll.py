class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        intersec_nums = []
        for i in set(nums1):
            if i in nums2 and i not in intersec_nums:
                intersec_nums.append(i)
            x = nums1.count(i)
            y = nums2.count(i)
            if x > 1 and y > 1:
                for j in range(min(x,y)-1):
                    intersec_nums.append(i)
        
        return intersec_nums
