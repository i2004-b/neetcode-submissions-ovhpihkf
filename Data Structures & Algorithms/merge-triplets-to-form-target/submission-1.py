class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        x, y, z = False, False, False 

        for triplet in triplets:
            if triplet[0] > target[0] or triplet[1] > target[1] or triplet[2] > target[2]:
                continue

            if triplet[0] == target[0]:
                x = True
            if triplet[1] == target[1]:
                y = True
            if triplet[2] == target[2]:
                z = True

        return (x and y and z)

            