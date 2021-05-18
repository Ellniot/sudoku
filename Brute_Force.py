#   ~~~ Brute Force Method ~~~
#
#   This algorithm provides every 
#   possible way to fill in a given 
#   sudoku puzzle, then removes the
#   illegal ones

from res.sudoku import Grid
import itertools


def brute_force(grid):
    # count the number of empty spaces
    cell_nums = []
    for i in range(80):
        cell_nums.append(grid.get_cell(i).get_num())
    empty_count = cell_nums.count(0)

    # create all permutations possible from 1-9 on the empty space list
    permutations = itertools.permutations('123456789', empty_count)
    for perm in permutations:
        print(str(perm) + "\n")

    # feed each permutation back into a grid

    # test each grid

    # return the first correct grid


def main():
    grid = Grid("030001000006000050500000983080006302000050000903800060714000009020000800000400030")

    #grid.print_grid()    
    brute_force(grid)

main()