class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        left = 0
        right = n-1
        while right>left:
            if numbers[left]+numbers[right]==target:
                break
            elif numbers[left]+numbers[right] < target:
                left = left+1
            elif numbers[left]+numbers[right] > target:
                right = right-1
        return [numbers[left], numbers[right]]
            