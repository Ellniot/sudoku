def convert_to_cell_num(x,y):
    return y*9+x

def convert_to_x_y(num):
    y = num // 9
    x = num % 9
    return (x, y)


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
            perm = (int(num_str[i]) != 0)

            self.cells.append(Cell(int(num_str[i]), perm, i))
        print("Cells created. len(self.cells) = " + str(len(self.cells)))

    def get_cell(self, cell_num):
        return self.cells[cell_num]

    def num_fits(self, x, y, region, num):
        #print("checking ("+str(x)+","+str(y)+") , r="+str(region)+"for num: "+str(num))
        
        cell_num = convert_to_cell_num(x, y)

        col_check = self.check_col(x, num, cell_num)
        row_check = self.check_row(y, num, cell_num)
        region_check = self.check_region(region, num, cell_num)

        #print("col_chk = "+str(col_check)+", row_chk = "+str(row_check)+", region_chk = "+str(region_check))

        return col_check and row_check and region_check

    # True = num will fit
    def check_col(self, x, num, cell_num):
        for i in range(len(self.cells)):
            # mod the cell # (0-80) by 9
            # x,y are 0-8
            if i % 9 == x:
                # don't compare the current cell
                if i != cell_num:
                    # cell is in the given col
                    if self.cells[i].get_num() == num:
                        return False
        return True

    def check_row(self, y, num, cell_num):
        for i in range(9):
            # debugging
            #print("row chk for cell #: " + str(y*9+i) + ", with num: " + str(num))
            #print(type(num))
            #print(type(self.cells[y*9+i].get_num()))
            # don't compare the current cell
                if (y*9+i) != cell_num:
                    if self.cells[y*9+i].get_num() == num:
                        return False
        return True

    def check_region(self, region, num, cell_num):
        for cell in self.cells:
            if cell.get_cell_num() != cell_num:
                if cell.get_region() == region:
                    if cell.get_num() == num:
                        return False
        return True

    def print_grid(self):
        output = ""
        for i in range(9):
            if i == 3 or i == 6:
                output = output + "---+---+---\n"
            for j in range(9):
                if j == 3 or j == 6:
                    output = output + "|"
                current_cell = self.cells[convert_to_cell_num(j,i)]
                current_cell_num = current_cell.get_num()
                if current_cell_num == 0:
                    output = output + " "
                else:
                    output = output + str(current_cell_num)
                if j == 8:
                    output = output + "\n"
        print(output)
        
    def is_complete(self):
        for cell in self.cells:
            if cell.get_num() == 0:
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
    
    # cell # (0-80)
    def get_cell_num(self):
        return self.cell_num

    # cell value (1-9)
    def get_num(self):
        return self.num
    
    def set_num(self, num):
        self.num = num
