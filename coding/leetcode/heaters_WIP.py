# https://leetcode.com/problems/heaters

class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:

        # Use a set to hold distinct houses, and remove houses from the set
        # once they are determined to be within the range of the heaters

        # Start with r=0, we can immediately remove the heater locations
        r = 0
        sh = set(houses) - set(heaters)
        ch = set()

        while sh:
            # Increase the radius and check remove any remaining houses within the radii
            r += 1
            for h in heaters:
                for i in range(h-r, h+r+1):
                    ch.add(i)

            sh = sh.difference(ch)
            ch.clear()
#            print(f'{r}: {sh}')

        return r

    ### above solution is taking too long -- because I am incrementing by one
    ### Could I start with the maximum possible radius
    ### r = (max(houses) - min(houses)) // 2 + 1
    ### then use bisection (or similar algorithm) to shorten it?

    ### Or, consider the fact that within the range of heaters, the maximum
    ### required radius is equal to half of the largest distance between
    ### adjacent heaters.  Outside of these bounds, the largest radius would
    ### be the distance between the lowest/highest heater and the last house
    ### in that same direction.

    # First check for houses that are outside of the range of heaters
    # This will define the minimum radius
    lower_range = abs(min(heaters) - min(houses))
    upper_range = abs(max(houses) - max(heaters))
    r_min = max(lower_range, upper_range)
    ### this will not work if the houses are more closely clustered to
    ### either of these heaters


