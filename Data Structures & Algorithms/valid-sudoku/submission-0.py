import collections
from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        subplots = [[], [], [], [], [], [], [], [], []]

        for i, row in enumerate(board):
            counts = collections.Counter(row)
            if i < 3:
                subplots[0].append(row[0:3])
                subplots[1].append(row[3:6])
                subplots[2].append(row[6:9])
            elif i >= 3 and i < 6:
                subplots[3].append(row[0:3])
                subplots[4].append(row[3:6])
                subplots[5].append(row[6:9])
            else:
                subplots[6].append(row[0:3])
                subplots[7].append(row[3:6])
                subplots[8].append(row[6:9])
            if 2 in counts.values():
                return False
        # Transpose and check for uniqueness
        transposed = list(zip(*board))
        for row in transposed:
            counts = collections.Counter(row)
            if 2 in counts.values():
                return False

        # Check 3x3 sub-matrices
        for box in subplots:
            combined = box[0] + box[1] + box[2]
            counts = collections.Counter(combined)
            if 2 in counts.values():
                return False
        return True