class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # Define our search boundaries
        low = max(weights)
        high = sum(weights)
        
        # This helper function checks if a given capacity is possible
        def can_ship_with_capacity(capacity):
            ships_needed = 1
            current_load = 0
            
            for w in weights:
                if current_load + w > capacity:
                    ships_needed += 1
                    current_load = 0
                current_load += w
                
            return ships_needed <= days

        # Binary search for the minimum valid capacity
        ans = high
        while low <= high:
            mid = (low + high) // 2
            
            if can_ship_with_capacity(mid):
                ans = mid       # This capacity works, but let's see if we can do better (smaller)
                high = mid - 1  # Shrink the search space to the lower half
            else:
                low = mid + 1   # This capacity is too small, we must go higher
                
        return ans