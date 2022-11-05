class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [0 for element in range(n)]
        for i in range(n):
            smaller_numbers_tally = 0
            for j in range(n):
                if j != i and nums[i] > nums[j]:
                    smaller_numbers_tally += 1
            output[i] = smaller_numbers_tally
        return output 
