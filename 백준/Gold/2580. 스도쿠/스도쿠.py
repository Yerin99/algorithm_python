def find_empty_cell_with_mrv(board, row_sets, col_sets, box_sets):
    """ 가능한 숫자가 가장 적은 빈 칸을 찾음 (MRV 전략) """
    min_options = float('inf')
    best_cell = None

    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                box_index = (row // 3) * 3 + (col // 3)
                possible_numbers = {num for num in range(1, 10)}
                
                # 가능한 숫자 집합 계산
                possible_numbers -= row_sets[row]
                possible_numbers -= col_sets[col]
                possible_numbers -= box_sets[box_index]

                # MRV 적용: 가능한 숫자가 가장 적은 칸 찾기
                if len(possible_numbers) < min_options:
                    min_options = len(possible_numbers)
                    best_cell = (row, col, possible_numbers)

    return best_cell  # (row, col, 가능한 숫자 집합)

def solve_sudoku(board):
    EMPTY = 0
    SIZE = 9

    # 빠른 유효성 검사를 위한 set 초기화
    row_sets = [set() for _ in range(SIZE)]
    col_sets = [set() for _ in range(SIZE)]
    box_sets = [set() for _ in range(SIZE)]

    # 기존 숫자들을 set에 미리 저장 (초기 상태)
    for row in range(SIZE):
        for col in range(SIZE):
            num = board[row][col]
            if num != EMPTY:
                box_index = (row // 3) * 3 + (col // 3)
                row_sets[row].add(num)
                col_sets[col].add(num)
                box_sets[box_index].add(num)

    def backtrack():
        cell = find_empty_cell_with_mrv(board, row_sets, col_sets, box_sets)
        if cell is None:  # 더 이상 빈 칸이 없으면 종료
            return True
        
        row, col, possible_numbers = cell
        box_index = (row // 3) * 3 + (col // 3)

        for num in possible_numbers:
            # 숫자 넣기
            board[row][col] = num
            row_sets[row].add(num)
            col_sets[col].add(num)
            box_sets[box_index].add(num)

            # 다음 단계 재귀 호출
            if backtrack():
                return True

            # 백트래킹 (되돌아가기)
            board[row][col] = EMPTY
            row_sets[row].remove(num)
            col_sets[col].remove(num)
            box_sets[box_index].remove(num)

        return False  # 모든 숫자 시도 후 실패

    return backtrack()

def print_sudoku_board(board):
    for row in board:
        print(" ".join(str(num) for num in row))

def input_sudoku_board():
    board = []
    for _ in range(9):
        row = list(map(int, input().split()))
        if len(row) != 9:
            raise ValueError("Each row must contain exactly 9 numbers.")
        board.append(row)
    return board

sudoku_board = input_sudoku_board()

if solve_sudoku(sudoku_board):
    print_sudoku_board(sudoku_board)
