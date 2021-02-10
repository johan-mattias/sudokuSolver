def check_boxes(p):

    corners = [p[0][0:3]+p[1][0:3]+p[2][0:3],
               p[0][3:6]+p[1][3:6]+p[2][3:6],
               p[0][6:9]+p[1][6:9]+p[2][6:9],
               p[3][0:3]+p[4][0:3]+p[5][0:3],
               p[3][3:6]+p[4][3:6]+p[5][3:6],
               p[3][6:9]+p[4][6:9]+p[5][6:9],
               p[6][0:3]+p[7][0:3]+p[8][0:3],
               p[6][3:6]+p[7][3:6]+p[8][3:6],
               p[6][6:9]+p[7][6:9]+p[8][6:9]]

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
    print('rows', rows)
    cols = check_cols(puzzle)
    print('cols', cols)
    boxes = check_boxes(puzzle)
    print('boxes', boxes)
    return rows and cols and boxes

def solve_iter(puzzle):

    solution = []
    '''
    print('original')
    for row in puzzle:
        print(row)
    '''
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
    '''
    print('remove rows')
    for row in solution:
        print(row)
    '''
    transpose = list(map(list, zip(*puzzle)))
    '''
    print('transpose')
    for row in transpose:
        print(row)
    '''
    solution_tr = []

    for indexY in range(len(transpose)):
        solution_tr.append([])
        for indexX in range(len(transpose[indexY])):
            solution_tr[indexY].append([])
            if transpose[indexY][indexX] == 0:
                solution_tr[indexY][indexX] = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                for number in transpose[indexY]:
                    if number in solution_tr[indexY][indexX]:
                        solution_tr[indexY][indexX].remove(number)
            else:
                solution_tr[indexY][indexX] = [transpose[indexY][indexX]]
    #print('solution_tr2')

    solution_tr2 = list(map(list, zip(*solution_tr)))
    '''
    for row in solution_tr2:
        print(row)
    '''
    corners = [[],[],[],[],[],[],[],[],[]]

    corners = [puzzle[0][0:3]+puzzle[1][0:3]+puzzle[2][0:3],
               puzzle[0][3:6]+puzzle[1][3:6]+puzzle[2][3:6],
               puzzle[0][6:9]+puzzle[1][6:9]+puzzle[2][6:9],
               puzzle[3][0:3]+puzzle[4][0:3]+puzzle[5][0:3],
               puzzle[3][3:6]+puzzle[4][3:6]+puzzle[5][3:6],
               puzzle[3][6:9]+puzzle[4][6:9]+puzzle[5][6:9],
               puzzle[6][0:3]+puzzle[7][0:3]+puzzle[8][0:3],
               puzzle[6][3:6]+puzzle[7][3:6]+puzzle[8][3:6],
               puzzle[6][6:9]+puzzle[7][6:9]+puzzle[8][6:9]]
    
    solution_bx = []

    for indexY in range(len(corners)):
        solution_bx.append([])
        for indexX in range(len(corners[indexY])):
            solution_bx[indexY].append([])
            if corners[indexY][indexX] == 0:
                solution_bx[indexY][indexX] = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                for number in corners[indexY]:
                    if number in solution_bx[indexY][indexX]:
                        solution_bx[indexY][indexX].remove(number)
            else:
                solution_bx[indexY][indexX] = [corners[indexY][indexX]]
    #print('solution_bx')
    #for row in solution_bx:
    #    print(row)

    solution_bx2 = [solution_bx[0][0:3]+solution_bx[1][0:3]+solution_bx[2][0:3],
               solution_bx[0][3:6]+solution_bx[1][3:6]+solution_bx[2][3:6],
               solution_bx[0][6:9]+solution_bx[1][6:9]+solution_bx[2][6:9],
               solution_bx[3][0:3]+solution_bx[4][0:3]+solution_bx[5][0:3],
               solution_bx[3][3:6]+solution_bx[4][3:6]+solution_bx[5][3:6],
               solution_bx[3][6:9]+solution_bx[4][6:9]+solution_bx[5][6:9],
               solution_bx[6][0:3]+solution_bx[7][0:3]+solution_bx[8][0:3],
               solution_bx[6][3:6]+solution_bx[7][3:6]+solution_bx[8][3:6],
               solution_bx[6][6:9]+solution_bx[7][6:9]+solution_bx[8][6:9]]
    '''
    print('solution_bx2')

    for row in solution_bx2:
        print(row)
    '''

    #TODO: intersect all possibilities

    solution_final = []

    for indexY in range(9):
        solution_final.append([])
        for indexX in range(9):
            #print(indexY, indexX)
            solution_final[indexY].append([])

            #print('set1', solution[indexY][indexX])
            #print('set2', solution_tr2[indexY][indexX])
            #print('set3', solution_bx2[indexY][indexX])

            temp = set(solution[indexY][indexX]).intersection(solution_tr2[indexY][indexX])

            temp2 = temp.intersection(solution_bx2[indexY][indexX])
            #print('tmp2', temp2)
    
            solution_final[indexY][indexX] = list(temp2)
    
    '''    print('final')
    for row in solution_final:
        print(row)
    ''' 
    #rows
    for y in range(len(solution_final)):
        for value in range(1,10):
            count = 0
            for options in solution_final[y]:
                for number in options:
                    if number == value:
                        count += 1
            if count == 1:
                for x in range(len(solution_final[y])):
                    if value in solution_final[y][x] and len(solution_final[y][x]) > 1:
                        print('row boom', y, x)
                        print(solution_final[y][x])
                        solution_final[y][x] = [value]
                        print(solution_final[y][x])

    '''print('final-after row')
    for row in solution_final:
        print(row)
    '''
    #cols
    #print('all these cols')
    solution_final_cols = list(map(list, zip(*solution_final)))

    for y in range(len(solution_final_cols)):
        for value in range(1,10):
            count = 0
            for options in solution_final_cols[y]:
                for number in options:
                    if number == value:
                        count += 1
            if count == 1:
                for x in range(len(solution_final_cols[y])):
                    if value in solution_final_cols[y][x] and len(solution_final_cols[y][x]) > 1:
                        print('col boom', y, x)
                        print(solution_final_cols[y][x])
                        solution_final_cols[y][x] = [value]
                        print(solution_final_cols[y][x])

    solution_final_cols_back = list(map(list, zip(*solution_final_cols)))

    '''print('final-after row')
    for row in solution_final_cols_back:
        print(row)
    print()
    #TODO:check boxes
    '''
    p = solution_final_cols_back.copy()

    solution_boxes = [p[0][0:3]+p[1][0:3]+p[2][0:3],
               p[0][3:6]+p[1][3:6]+p[2][3:6],
               p[0][6:9]+p[1][6:9]+p[2][6:9],
               p[3][0:3]+p[4][0:3]+p[5][0:3],
               p[3][3:6]+p[4][3:6]+p[5][3:6],
               p[3][6:9]+p[4][6:9]+p[5][6:9],
               p[6][0:3]+p[7][0:3]+p[8][0:3],
               p[6][3:6]+p[7][3:6]+p[8][3:6],
               p[6][6:9]+p[7][6:9]+p[8][6:9]]
    '''
    print('debug')
    for row in solution_boxes:
        print(row)
    '''
    for y in range(len(solution_boxes)):
        for value in range(1,10):
            count = 0
            for options in solution_boxes[y]:
                for number in options:
                    if number == value:
                        count += 1
            if count == 1:
                for x in range(len(solution_boxes[y])):
                    if value in solution_boxes[y][x] and len(solution_boxes[y][x]) > 1:
                        print('boom boxes')
                        print(solution_boxes[y][x])
                        solution_boxes[y][x] = [value]
                        print(solution_boxes[y][x])

    solution_boxes_2 = [solution_boxes[0][0:3]+solution_boxes[1][0:3]+solution_boxes[2][0:3],
            solution_boxes[0][3:6]+solution_boxes[1][3:6]+solution_boxes[2][3:6],
            solution_boxes[0][6:9]+solution_boxes[1][6:9]+solution_boxes[2][6:9],
            solution_boxes[3][0:3]+solution_boxes[4][0:3]+solution_boxes[5][0:3],
            solution_boxes[3][3:6]+solution_boxes[4][3:6]+solution_boxes[5][3:6],
            solution_boxes[3][6:9]+solution_boxes[4][6:9]+solution_boxes[5][6:9],
            solution_boxes[6][0:3]+solution_boxes[7][0:3]+solution_boxes[8][0:3],
            solution_boxes[6][3:6]+solution_boxes[7][3:6]+solution_boxes[8][3:6],
            solution_boxes[6][6:9]+solution_boxes[7][6:9]+solution_boxes[8][6:9]]
    '''print('after boxes')
    for row in solution_boxes:
        print(row)
    '''
    return solution_boxes_2
    
def solve(puzzle):

    print('puzzle')
    for row in puzzle:
        print(row)

    count = 0
    while count < 6:
        solution = solve_iter(puzzle)
        '''
        print('solution')
        for row in solution:
            print(row)
        '''
        for indexY in range(len(solution)):
            for indexX in range(len(solution[indexY])):
                if len(solution[indexY][indexX]) == 1:
                    puzzle[indexY][indexX] = solution[indexY][indexX][0]

        print('round: ', count)
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
    puzzle = [[0,0,0, 0,0,0, 0,7,0],
              [0,7,0, 0,0,3, 8,0,0],
              [0,0,0, 0,6,0, 0,5,0],

              [0,2,0, 9,0,0, 7,8,0],
              [0,0,0, 7,0,1, 0,3,0],
              [0,0,0, 0,3,0, 9,0,0],

              [0,6,0, 0,7,0, 0,4,0],
              [1,0,0, 0,0,9, 0,0,0],
              [3,0,9, 0,0,4, 0,0,0]]
               
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

    print(is_finished(puzzle))

    for row in puzzle:
        print(row)
    solve(puzzle)


run()