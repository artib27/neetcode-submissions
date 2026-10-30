class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # if len(set(nums)) == len(nums):
        #     return False
        # return True
        visited = set()

        for num in nums :
            if num in visited:
                return True
            visited.add(num)   
        return False 