class Solution:
    def numberOfWeakCharacters(self, properties):
        
        # Sort by attack ascending
        # If attack is same, defense descending
        properties.sort(key=lambda x: (x[0], -x[1]))

        maxDefense = 0
        count = 0

        # Traverse from right to left
        for i in range(len(properties) - 1, -1, -1):

            if properties[i][1] < maxDefense:
                count += 1

            maxDefense = max(maxDefense, properties[i][1])

        return count