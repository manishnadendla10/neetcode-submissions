class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
      num_to_target = {}

      for i, num in enumerate(nums):
        complement = target - num 

        if complement in num_to_target:
                return [num_to_target[complement], i ]
        
        num_to_target[num] = i 
    
      return[]