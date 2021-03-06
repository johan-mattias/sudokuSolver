debug = False

def box_transform(p):
    ''' Returns the matrix as rows of boxes '''
    p_boxes = [p[0][0:3]+p[1][0:3]+p[2][0:3],
               p[0][3:6]+p[1][3:6]+p[2][3:6],
               p[0][6:9]+p[1][6:9]+p[2][6:9],
               p[3][0:3]+p[4][0:3]+p[5][0:3],
               p[3][3:6]+p[4][3:6]+p[5][3:6],
               p[3][6:9]+p[4][6:9]+p[5][6:9],
               p[6][0:3]+p[7][0:3]+p[8][0:3],
               p[6][3:6]+p[7][3:6]+p[8][3:6],
               p[6][6:9]+p[7][6:9]+p[8][6:9]]
    return p_boxes

def transform(puzzle):
    ''' Transforms columns to rows'''
    return list(map(list, zip(*puzzle)))
 

def check_boxes(p):
    '''Returns the possibilities of the puzzle from boxes'''
    corners = box_transform(p)
    result = check_rows(corners)
    return result


def check_rows(puzzle):
    '''Return True if all numbers exist in a row'''
    for row in puzzle:
        for number in range(1,10):
            if not number in row:
                return False
    return True


def check_cols(puzzle):
    '''Return True if all numbers exist in a column'''

    transpose = transform(puzzle)

    for row in transpose:
        for number in range(1,10):
            if not number in row:
                return False
    return True

def is_finished(puzzle):
    rows = check_rows(puzzle)
    print('rows', rows)
    cols = check_cols(puzzle)
    print('cols', cols)
    boxes = check_boxes(puzzle)
    print('boxes', boxes)
    return rows and cols and boxes

def find_solution(puzzle):
    solution = []
    for indexY in range(len(puzzle)):
        solution.append([])
        for indexX in range(len(puzzle[indexY])):
            solution[indexY].append([])
            if puzzle[indexY][indexX] == 0:
                solution[indexY][indexX] = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                for number in puzzle[indexY]:
                    if number in solution[indexY][indexX]:
                        solution[indexY][indexX].remove(number)
            else:
                solution[indexY][indexX] = [puzzle[indexY][indexX]]
    return solution

def simplify(solution, kind='row'):

    if debug:
        print('simplify', kind)
        for row in solution:
            print(row)

    for y in range(len(solution)):
        instance = dict()
        for value in range(1,10):
            count = 0
            for options in solution[y]:
                for number in options:
                    if number == value:
                        count += 1
            instance[value] = count
            if count == 1:
                for x in range(len(solution[y])):
                    if value in solution[y][x] and len(solution[y][x]) > 1:
                        print(kind,' boom', y, x)
                        print(solution[y][x])
                        solution[y][x] = [value]
                        print(solution[y][x])
        #print('instance', kind)
        #print(instance)

        double = []
        for key, value in instance.items():
            if value == 2:
                double.append(key)
        if len(double) > 1:
            #print(double)
            #check if they are from the same intersection
            check = []
            for val_index in range(len(double)):
                check.append([])
                for index in range(len(solution[y])):
                    if double[val_index] in solution[y][index]:
                        check[val_index].append(index)
            #print(solution[y])
            #print('check')
            #print(check)
            match_index = []
            for index1 in range(len(check)):
                for index2 in range(len(check)):
                    if index1 != index2 and set(check[index1]) == set(check[index2]) and index1<index2:
                        #print('match', double[index1], double[index2])
                        match_index.append(double[index1])
                        match_index.append(double[index2])

                        for op_index in range(len(solution[y])):
                            if double[index1] in solution[y][op_index] and double[index2] in solution[y][op_index]:
                                print('boom, lock')
                                print(double[index1], double[index2], solution[y][op_index] )
                                solution[y][op_index] = [double[index1], double[index2]]
                                print(solution[y][op_index])

                                pass

    for row in solution:
        print(row)

                        
    return solution

def intersect_solution(row, col, box):
    solution = []

    if debug:
        print('intersect - row')
        for row1 in row:
            print(row1)
        print('intersect - col')
        for row2 in col:
            print(row2)
        print('intersect - box')
        for row3 in box:
            print(row3)


    for indexY in range(9):
        solution.append([])
        for indexX in range(9):
            solution[indexY].append([])
            temp = set(row[indexY][indexX]).intersection(col[indexY][indexX])
            temp2 = list(temp.intersection(box[indexY][indexX]))
            #TODO: check if there's an assignment by intersection
            solution[indexY][indexX] = temp2
    
    if True:
        print('solution intersect')
        for row4 in solution:
            print(row4)

    solution = simplify(solution, 'row')
    solution = transform(simplify(transform(solution), 'col'))
    solution = box_transform(simplify(box_transform(solution), 'box'))

    return solution

def assign(puzzle, solution):
    for indexY in range(len(solution)):
        for indexX in range(len(solution[indexY])):
            if len(solution[indexY][indexX]) == 1:
                #TODO: make sure that assignment does create a conflict
                puzzle[indexY][indexX] = solution[indexY][indexX][0]
    return puzzle

def solve_iter(puzzle):

    row_solution = find_solution(puzzle)
    col_solution = transform(find_solution(transform(puzzle)))
    box_solution = box_transform(find_solution(box_transform(puzzle)))

    solution = intersect_solution(row_solution, col_solution, box_solution)

    if debug:
        for row in solution:
            print(row[0:3], "\t", row[3:6], "\t", row[6:9], "\t")

    return assign(puzzle, solution)

    
def solve(puzzle):
    count = 0
    while count < 8:
        print('round', count)
        puzzle = solve_iter(puzzle)

        for row in puzzle:
            print(row)

        count += 1

def run():
    '''
    puzzle = [[0,0,0, 0,9,0, 0,7,0],
              [0,7,0, 0,1,3, 8,9,0],
              [0,0,0, 0,6,7, 0,5,0],

              [0,2,3, 9,0,0, 7,8,1],
              [0,0,0, 7,0,1, 0,3,0],
              [7,0,0, 0,3,0, 9,0,0],

              [0,6,0, 1,7,0, 3,4,9],
              [1,4,7, 3,0,9, 0,0,8],
              [3,0,9, 6,0,4, 0,1,7]]

              [0, 0, 0, 0, 9, 0, 0, 7, 0]
              [0, 7, 0, 0, 1, 3, 8, 9, 0]
              [0, 0, 0, 0, 6, 7, 0, 5, 0]
              [0, 2, 3, 9, 0, 0, 7, 8, 1]
              [0, 0, 0, 7, 0, 1, 0, 3, 0]
              [7, 0, 0, 0, 3, 0, 9, 0, 0]
              [0, 6, 0, 1, 7, 0, 3, 4, 9]
              [1, 4, 7, 3, 0, 9, 0, 0, 8]
              [3, 0, 9, 6, 0, 4, 0, 1, 7]
    '''
    '''
    puzzle = [[0,0,0, 0,0,0, 0,7,0],
              [0,7,0, 0,0,3, 8,0,0],
              [0,0,0, 0,6,0, 0,5,0],

              [0,2,0, 9,0,0, 7,8,0],
              [0,0,0, 7,0,1, 0,3,0],
              [0,0,0, 0,3,0, 9,0,0],

              [0,6,0, 0,7,0, 0,4,0],
              [1,0,0, 0,0,9, 0,0,0],
              [3,0,9, 0,0,4, 0,0,0]]
    '''
    puzzle = [[0,0,7,3,0,0,8,4,0],
              [0,6,0,0,8,0,0,0,3],
              [0,0,0,0,0,5,9,7,0],
              [0,0,5,9,7,0,0,0,0],
              [3,0,0,0,1,8,0,0,9],
              [0,4,0,0,0,6,0,0,2],
              [2,0,0,0,0,0,4,0,0],
              [0,0,4,0,0,0,0,0,0],
              [0,5,6,0,0,7,0,0,0]]
               
    solved = [[1,2,3, 4,5,6, 7,8,9],
              [4,5,6, 7,8,9, 1,2,3],
              [7,8,9, 1,2,3, 4,5,6],

              [2,3,4, 5,6,7, 8,9,1],
              [5,6,7, 8,9,1, 2,3,4],
              [8,9,1, 2,3,4, 5,6,7],

              [3,4,5, 6,7,8, 9,1,2],
              [6,7,8, 9,1,2, 3,4,5],
              [9,1,2, 3,4,5, 6,7,8,]]

    #print(is_finished(solved))

    #print(is_finished(puzzle))

    for row in puzzle:
        print(row)
    solve(puzzle)


run()