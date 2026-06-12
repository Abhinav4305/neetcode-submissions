class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        n = len(people)
        count = 0
        people.sort()
        left = 0
        right = n-1
        while left <= right:
            rem = limit - people[right]
            right -= 1
            count += 1
            if left <= right and rem >= people[left]:
                left += 1
            
        return count


        