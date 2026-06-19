class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)
        hash_map={}
        for i in range(0,n):
            remains=target-nums[i]
            if remains in hash_map:
                return [hash_map[remains],i]
            else:
                hash_map[nums[i]]=i
