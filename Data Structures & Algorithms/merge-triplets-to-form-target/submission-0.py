class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        make_one = make_two = make_three = False

        for trip in triplets:
            if trip[0] > target[0] or trip[1] > target[1] or trip[2] > target[2]:
                continue
            
            if trip[0] == target[0]:
                make_one = True
            if trip[1] == target[1]:
                make_two = True
            if trip[2] == target[2]:
                make_three = True

        return make_one and make_two and make_three