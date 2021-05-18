    # ~~~ Guided Recursion ~~~
    #
    # This algorithm uses recursion
    # to provide a guided brute force
    # solution to a given sudoku puzzle

# input: 81 char sting of ints representing an unsolved sudoku board
#       note: blanks should be entered as 0

# output: 81 char sting representing the same solved sudoku board

from res.sudoku import convert_to_cell_num
from res.sudoku import Grid


# get the next cell pos based on the current pos
def get_next(x, y, format="tup"):
        if x == 8:
            next_x = 0
            next_y = y+1
        else:
            next_x = x+1
            next_y = y
        if format !="tup":
            return convert_to_cell_num(next_x, next_y)
        return next_x, next_y


def guess_cell(cell, grid):
    current_x = cell.get_x()
    current_y = cell.get_y()

    # check if the grid is complete
    if grid.is_complete():
        return grid

    # check if the cell should be skipped
    if cell.has_perm_num() and not cell.is_last():
        next_cell = get_next(current_x, current_y, format="num")
        guess_cell(grid.get_cell(next_cell), grid)

    # try numbers in the current cell
    else:
        # 1-10 b/c spaces will be filled with nums 1-9, not 0-8
        for i in range(1,10):
            region = cell.get_region()
            num_found = grid.num_fits(current_x, current_y, region, i)
            if num_found:
                cell.set_num(i)
                if not cell.is_last():
                    next_cell = get_next(current_x, current_y, format="num")
                    guess_cell(grid.get_cell(next_cell), grid)
                    if not grid.is_complete():
                        cell.set_num(0)
    return grid

def main():
    grid = Grid("030001000006000050500000983080006302000050000903800060714000009020000800000400030")
    grid.print_grid()
    finished_grid = guess_cell(grid.get_cell(0), grid)
    finished_grid.print_grid()
    print(grid.get_solution())

main()