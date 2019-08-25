

nums = ['1','2','3','4','5','6','7','8','9']
ints = [1,2,3,4,5,6,7,8,9]

def get_row(row_num):
    return puzzle[row_num]

def get_column(column_num):
    return [row[column_num] for row in puzzle]

def get_square(row, column):
    row_chunk = 3 * int(row/3)
    col_chunk = 3 * int(column/3)
    ret = []
    for row in puzzle[row_chunk:row_chunk+3]:
        ret += row[col_chunk:col_chunk+3]
    return ret

def perms(row, column):
    if puzzle[row][column] !='0':
        raise Exception("Permission matricolumn requested for nonzero square (" + str(column) + "," + str(row) + "), value: " + puzzle[row][column])
    ret = nums
    ret = [num for num in ret if num not in get_row(row)]
    ret = [num for num in ret if num not in get_column(column)]
    ret = [num for num in ret if num not in get_square(row,column)]
    return ret

def print_puzzle():
    for i in range(0,9):
        print()
        if i%3 == 0:
            print()
        for j in range(0,9):
            if j%3 == 0:
                print(" ", end="")
            print(puzzle[i][j], end="")
    print()

def check_puzzle():
    for row in puzzle:
        for value in row:
            if value == '0':
                raise Exception("Puzzle is incomplete.")
    for i in range(0,9):
        if sum(map(int,get_column(i))) != 45 or sum(map(int,get_row(i))) != 45:
            raise Exception("Row or column found with improper sum.")
    for i in range(0,9,3):
        for j in range(0,9,3):
            if sum(map(int,get_square(i,j))) != 45:
                raise Exception("Square found with improper sum.")

fin = open("puzzles.txt")

puzzles = fin.readlines()
puzzle = puzzles[1:10]

puzzle = [list(row.strip()) for row in puzzle]

print_puzzle()

todo = 0
for row in puzzle:
    for value in row:
        if value == '0':
            todo += 1

while todo > 0:
    for row in range(0,9):
        for column in range(0,9):
            if puzzle[row][column] == '0' and len(perms(row,column)) == 1:
                puzzle[row][column] = perms(row,column)[0]
                todo -= 1
check_puzzle()
print_puzzle()



