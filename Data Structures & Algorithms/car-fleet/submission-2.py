class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        # take the closest car to target
        # gather all of the faster cars right behind its position in a row
        # for each of the ones who will catch up make it into a fleet
        # they will catch up if target-position / speed is smaller than the closest car in the fleet's time to target
        hashmap = {}
        fleets = 1
        highest = 0
        
        for i in range(n):
            hashmap[position[i]] = i
            highest = max(highest, position[i])
        fleet_start = hashmap[highest]

        for key in sorted(hashmap, reverse=True):
            if (target - position[fleet_start]) / speed[fleet_start] < (target - key) / speed[hashmap[key]]:
                fleets += 1
                fleet_start = hashmap[key]
        return fleets 
            

