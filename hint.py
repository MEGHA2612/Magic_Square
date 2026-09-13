# --------------------------------
# HINT SYSTEM
# --------------------------------
MAGIC_SQUARE_SOLUTION = [
    [8, 1, 6],
    [3, 5, 7],
    [4, 9, 2]
]

# --------------------------------
# FIND HINT
# --------------------------------
def get_hint(grid):
    for row in range(3):
        for col in range(3):
            if grid[row][col] == 0:
                return {
                    "row": row,
                    "col": col,
                    "value": MAGIC_SQUARE_SOLUTION[row][col]
                }
    return None