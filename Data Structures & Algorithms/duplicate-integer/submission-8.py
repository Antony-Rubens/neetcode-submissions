class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        length = len(nums)
        res = set(nums)
        if len(res)== length:
            return False
        return True
