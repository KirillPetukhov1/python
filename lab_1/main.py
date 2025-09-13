# from types import Arr
import unittest

def find_sum(nums, target: int):
    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return None

class TestMath(unittest.TestCase):
    def test_no_answer(self):
        self.assertEqual(find_sum([1, 2], 10), None)
    def test_one_answer(self):
        self.assertEqual(find_sum([1, 2, 8, 3], 5), [1, 3])
    def test_more_one_answer(self):
        self.assertEqual(find_sum([2, 5, 7, 6, 4, 9, 6], 12), [1, 2])

unittest.main(argv=[''], verbosity=2, exit=False)