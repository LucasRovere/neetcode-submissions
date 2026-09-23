class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        first_possible = False
        second_possible = False
        third_possible = False

        for triplet in triplets:
            if triplet[0] == target[0] and triplet[1] <= target[1] and triplet[2] <= target[2]:
                first_possible = True
            if triplet[0] <= target[0] and triplet[1] == target[1] and triplet[2] <= target[2]:
                second_possible = True
            if triplet[0] <= target[0] and triplet[1] <= target[1] and triplet[2] == target[2]:
                third_possible = True

            if first_possible and second_possible and third_possible:
                return True

        return first_possible and second_possible and third_possible
        