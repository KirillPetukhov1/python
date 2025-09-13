from typing import Optional, List
import unittest

def find_sum(nums: List[int], target: int) -> Optional[List[int]]:
    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            try:
                if int(nums[i]) + int(nums[j]) == target:
                    return [i, j]
            except ValueError:
                return None
    return None

class TestFindSum(unittest.TestCase):
    def test_1(self):
        self.assertEqual(find_sum([2, 7, 11, 15], 9), [0, 1])
    
    def test_2(self):
        self.assertEqual(find_sum([3, 2, 4], 6), [1, 2])
    
    def test_3(self):
        self.assertEqual(find_sum([3, 3], 6), [0, 1])
    
    def test_no_answer(self):
        self.assertEqual(find_sum([1, 2], 10), None)
    
    def test_one_answer(self):
        self.assertEqual(find_sum([1, 2, 8, 3], 5), [1, 3])
    
    def test_more_one_answer(self):
        self.assertEqual(find_sum([2, 5, 7, 6, 4, 9, 6], 12), [1, 2])
    
    def test_empty_nums(self):
        self.assertEqual(find_sum([], 10), None)

    def test_float_in_nums(self):
        self.assertEqual(find_sum([1, 2.34, 8, 3.68], 5), [1, 3])

    def test_str_in_nums(self):
        self.assertEqual(find_sum(['dsf', 'sd', 8, 3.68], 5), None)

unittest.main(argv=[''], verbosity=2, exit=False)