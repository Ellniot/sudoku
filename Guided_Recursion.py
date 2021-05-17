# TODO - replace "box num" with "region"
# TODO add exception to comparison for 0


class Grid:
    def __init__(self, cells):
        self.cells = []
        self.create_cells(cells)
        # Arrangement of cell pos in sudoku grid
        #
        #    0- 2   |    3- 5   |    6- 8
        #    9-11   |   12-14   |   15-17
        #   18-20   |   21-23   |   24-26
        #   -----------------------------
        #   27-29   |   30-32   |   33-35
        #   36-38   |   39-41   |   42-44
        #   45-47   |   48-50   |   51-53
        #   -----------------------------
        #   54-56   |   57-59   |   60-62
        #   63-65   |   66-68   |   69-71
        #   72-74   |   75-77   |   78-80

    def create_cells(self, num_str):
        for i in range(len(num_str)):
            perm = (num_str[i] != 0)

            self.cells.append(Cell(num_str[i], perm, i))
        print("Cells created. len(self.cells) = " + str(len(self.cells)))

    def get_cell(self, cell_num):
        return self.cells[cell_num]

    def num_fits(self, x, y, region, num):
        return self.check_col(x, num) \
            and self.check_row(y, num) \
            and self.check_region(region, num)

    # True = num will fit
    def check_col(self, x, num):
        for i in range(len(self.cells)):
            # mod the cell # (0-80) by 9
            # x,y are 0-8
            if i % 9 == x:
                # cell is in the given col
                if self.cells[i].get_num() == num:
                    return False
        return True

    def check_row(self, y, num):
        for i in range(9):
            if self.cells[y*9+i] == num:
                return False
        return True

    def check_region(self, region, num):
        for cell in self.cells:
            if cell.get_region() == region:
                if cell.get_num() == num:
                    return False
        return True


class Cell:
    def __init__(self, num, is_perm, cell_num):
        self.num = num
        self.is_perm = is_perm
        self.x = convert_to_x_y(cell_num)[0]
        self.y = convert_to_x_y(cell_num)[1]
        self.cell_num = cell_num
        self.region = self.get_region_num(cell_num,9,9,3,3)

    # assuming cells are a l-to-r list, top-to-bottom, starting from 0
    # built this out to be beefier than needed
    def get_region_num(self, cell_num, row_count, col_count, region_row_count, region_col_count):
        # get the row, 0 = first row
        row = cell_num // col_count
        # get the col, 0 = first col
        col = cell_num % row_count
        # get the region x pos
        region_x_pos = col // region_col_count
        # get the region y pos
        region_y_pos = row // region_row_count
        # combine the two to get the region
        region = region_y_pos * region_col_count + region_x_pos
        return region

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_region(self):
        return self.region

    def has_perm_num(self):
        return self.is_perm

    def is_last(self):
        return (self.x == 8 and self.y == 8)
    
    def get_num(self):
        return self.num
    
    def set_num(self, num):
        self.num = num


def convert_to_cell_num(x,y):
    return y*9+x

def convert_to_x_y(num):
    y = num // 9
    x = num % 9
    return (x, y)

# get the next cell pos based on the current pos
def get_next(x, y):
        if x == 8:
            next_x = 0
            next_y = y+1
        else:
            next_x = x+1
            next_y = y
        
        return (next_x, next_y)


def guess_cell(cell, grid):
    current_x = cell.get_x()
    current_y = cell.get_y()
    if cell.has_perm_num():
        if not cell.is_last():
            guess_cell(get_next(current_x, current_y))
        else:
            x = input()
    else:
        num_found = False
        # 1-10 b/c spaces will be filled with nums 1-9, not 0-8
        for i in range(0,10):
            # in case the cell needs to be changed after being set
            cell.set_num(0)
            region = cell.get_region()
            num_found = grid.num_fits(current_x, current_y, region, i)
            if num_found and not cell.is_last():
                cell.set_num(i)
                next_cell = convert_to_cell_num(get_next(current_x, current_y))
                guess_cell(grid.get_cell(next_cell), grid)
            else:
                x = input()
        if not num_found:
            return

def main():
    grid = Grid("030001000006000050500000983080006302000050000903800060714000009020000800000400030")

main()