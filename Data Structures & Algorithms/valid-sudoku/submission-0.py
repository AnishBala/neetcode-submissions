# row contains 1-9
# col contains 1-9
# board must be 3x3


# for each row check no duplicates, O(n)
# for each col check no duplicates, O(n)
# take each 3 x 3 check no duplicates
from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        isValid = False
        row = defaultdict(set)
        col = defaultdict(set)
        box = defaultdict(set)

        for r in range(9):
            for c in range(9):
                value = board[r][c]
                if value == ".":
                    continue
                b = (r // 3, c // 3)
                if value in row[r] or value in col[c] or value in box[b]:
                    return False
                row[r].add(value)
                col[c].add(value)
                box[b].add(value)
        return True
        