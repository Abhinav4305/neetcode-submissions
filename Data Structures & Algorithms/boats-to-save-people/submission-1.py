class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        n = len(people)
        count = 0
        people.sort()
        left = 0
        right = n-1
        while left <= right:
            if people[left]+people[right] == limit:
                count += 1
                left += 1
                right -= 1
            elif people[left]+people[right] > limit:
                count += 1
                right -= 1
        return count


        