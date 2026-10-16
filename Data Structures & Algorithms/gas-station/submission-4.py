class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        """
        Brute force: go around and start from each location
        go around starting from each location
            from that location iterate i times
                set variable to 0 for the total gas
                pair up the gas and the cost 
                    add the gas amount to the total and then subtract the cost to get to the next place
                        if that's neg: break

            if gas is positive or 0:
                return that index

        return -1 

        length = len(gas)

        for i in range(length):
            gas_needed = 0

            for j in range(length):
                if i + j >= length:
                    ind = (i + j) % length
                else:
                    ind = i + j

                gas_needed += gas[ind]
                gas_needed -= cost[ind]

                if gas_needed < 0:
                    break

            if gas_needed >= 0:
                return i

        return -1
        """
        if sum(cost) > sum(gas):
            return -1
            
        index = 0
        tracker = 0

        for i in range(len(gas)):
            if tracker < 0:
                tracker = 0
                index = i

            tracker += (gas[i] - cost[i])

        return index

        


