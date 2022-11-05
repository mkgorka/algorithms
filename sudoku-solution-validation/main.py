def valid_solution(board):
    counter = 0

    for element in board:
        if element == 0:
            counter += 1
            if counter >= 2:
                return False
