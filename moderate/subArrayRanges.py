class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(2, n):
            pass


# 4 -2;-2 -3;-3 4;4 1
# 4 -2 -3;
nums = []
obj = Solution()
res = obj.subArrayRanges(nums)
print(res)
