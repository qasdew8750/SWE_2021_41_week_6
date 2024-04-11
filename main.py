from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    length = len(nums)
    for i in range(length):
      for j in range(length):
        if(i == j):
          continue
        if(nums[i] + nums[j] == target):
          return[nums[i], nums[j]]
