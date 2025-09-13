from typing import Optional, List

def find_sum(nums: List[int], target: int) -> Optional[List[int]]:
    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            try:
                if int(nums[i]) + int(nums[j]) == target:
                    return [i, j]
            except ValueError:
                return None
    return None