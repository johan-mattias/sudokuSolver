def check_boxes(puzzle):

    corners = [[],[],[],[],[],[],[],[],[]]

    count = 0
    index = 0

    for indexY in range(len(puzzle)):
        for indexX in range(len(puzzle[indexY])):
            corners[index].append(puzzle[indexY][indexX])
            if count < 2:
                count += 1
            else:
                count = 0
                if index < 8:
                    index += 1
                else:
                    index = 0
    
    result = check_rows(corners)
    return result


def check_rows(puzzle):
    for row in puzzle:
        for number in range(1,10):
            if not number in row:
                return False
    return True


def check_cols(puzzle):
    transpose = list(map(list, zip(*puzzle)))

    for row in transpose:
        for number in range(1,10):
            if not number in row:
                return False
    return True

def is_finished(puzzle):


    rows = check_rows(puzzle)
    cols = check_cols(puzzle)
    boxes = check_boxes(puzzle)

    return rows and cols and boxes

def solve():

    puzzle = [[0,0,0,0,9,0,0,7,0],
              [0,7,0,0,1,3,8,9,0],
              [0,0,0,0,6,7,0,5,0],
              [0,2,3,9,0,0,7,8,1],
              [0,0,0,7,0,1,0,3,0],
              [7,0,0,0,3,0,9,0,0],
              [0,6,0,1,7,0,3,4,9],
              [1,4,7,3,0,9,0,0,8],
              [3,0,9,6,0,4,0,1,7]]
              
    solved = [[1,2,3,4,5,6,7,8,9],
              [2,3,4,5,6,7,8,9,1],
              [3,4,5,6,7,8,9,1,2],
              [4,5,6,7,8,9,1,2,3],
              [5,6,7,8,9,1,2,3,4],
              [6,7,8,9,1,2,3,4,5],
              [7,8,9,1,2,3,4,5,6],
              [8,9,1,2,3,4,5,6,7],
              [9,1,2,3,4,5,6,7,8,]]

    print(is_finished(solved))

    print(is_finished(puzzle))


solve()