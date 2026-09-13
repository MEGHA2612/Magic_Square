# --------------------------------
# MAGIC SQUARE VALIDATION
# --------------------------------
def check_numbers(grid):
    """
    Check whether the grid contains
    all numbers from 1 to 9 exactly once.
    """
    numbers = []
    for row in grid:
        for value in row:
            numbers.append(value)

    # Check for empty cells
    if 0 in numbers:
        return False, "Some cells are still empty."

    # Check numbers 1-9
    if sorted(numbers) != list(range(1, 10)):
        return False, ("Use every number from 1 to 9 " "exactly once.")
    return True, ""

def check_rows(grid, target):
    """
    Check every row.
    """
    for row_index, row in enumerate(grid):
        row_sum = sum(row)
        if row_sum != target:
            return False, (
                f"Row {row_index + 1} "
                f"has sum {row_sum}. "
                f"It should be {target}."
            )

    return True, ""

def check_columns(grid, target):
    """
    Check every column.
    """
    size = len(grid)
    for col in range(size):
        column_sum = 0
        for row in range(size):
            column_sum += grid[row][col]
        if column_sum != target:
            return False, (
                f"Column {col + 1} "
                f"has sum {column_sum}. "
                f"It should be {target}."
            )
        
    return True, ""

def check_diagonals(grid, target):
    """
    Check both diagonals.
    """
    size = len(grid)
    # Main diagonal
    diagonal_1 = 0
    for i in range(size):
        diagonal_1 += grid[i][i]

    if diagonal_1 != target:
        return False, (
            f"Main diagonal has sum "
            f"{diagonal_1}. "
            f"It should be {target}."
        )

    # Other diagonal
    diagonal_2 = 0
    for i in range(size):
        diagonal_2 += grid[i][size - 1 - i]

    if diagonal_2 != target:
        return False, (
            f"Other diagonal has sum "
            f"{diagonal_2}. "
            f"It should be {target}."
        )

    return True, ""

def validate_magic_square(grid, target):
    """
    Perform all validation checks.
    """
    # Check numbers
    valid, message = check_numbers(grid)
    if not valid:
        return False, message

    # Check rows
    valid, message = check_rows(grid, target)
    if not valid:
        return False, message

    # Check columns
    valid, message = check_columns(grid, target)
    if not valid:
        return False, message

    # Check diagonals
    valid, message = check_diagonals(grid,target)
    if not valid:
        return False, message

    # Everything passed
    return True, ("🎉 Congratulations! " "You completed the Magic Square!")