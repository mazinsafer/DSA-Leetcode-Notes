## O(n^2) time but since a sudoku board is always 9x9 its fixed and small so theres a constant sized input (81) so O(1)
## O(1) space
class Solution(object):
    def isValidSudoku(self, board):
        rows = {}
        columns = {}
        boxes = {}
        for i, row in enumerate(board):
            for j, cell in enumerate(row):
                box_index = (i // 3, j // 3)
                if cell == ".":
                    continue
                if i not in rows:
                    rows[i] = set()
                if cell in rows[i]:
                    return False
                else:
                    rows[i].add(cell)
                if j not in columns:
                    columns[j] = set()
                if cell in columns[j]:
                    return False
                else:
                    columns[j].add(cell)
                if box_index not in boxes:
                    boxes[box_index] = set()
                if cell in boxes[box_index]:
                    return False
                else:
                    boxes[box_index].add(cell)
                   
        return True
                    

## first initialize 3 hashmaps, 1 to keep track of numbers seen in rows, for columns, and for the 3x3 boxes
## first iterate through the rows and its index
## within that row you iterate through the cells and index of the cells
## to get the box index you do floor division of cell index and column index by 3 because the box is 3,3.
    ## for example the cell at 0,1 corresponds to row at index 0, column at index 1 (first row, second column)
## skip to the next cell if its empty (".")
## each hashmap will have the key-value pair of row/col/box index number: set of all the numbers seen in that row/col/box
## so if the curr index of row/col/box is not in the hashmap, add it and initialize a set of seen numbers
    ## if the number in the cell is a number already in the set, return False because there cant be repeats
    ##  if the number in the cell isnt in the set, add it
## if you can get through each row, column, and box return True