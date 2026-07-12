class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        prev=nums[0]+nums[1]
        count=1
        i=2
        while i<=len(nums)-2:
            if nums[i]+nums[i+1]==prev:
                count+=1
                i+=2
            else:
                break
        return count
                    