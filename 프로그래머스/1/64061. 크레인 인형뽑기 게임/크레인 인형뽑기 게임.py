def solution(board, moves):
    basket = []
    count = 0
    
    for col in moves:
        for row in range(len(board)):
            if board[row][col-1] == 0:
                continue
            else:
                basket.append(board[row][col-1])
                board[row][col-1] = 0
            
            if len(basket) >= 2:
                if basket[-1] == basket[-2]:
                    basket.pop()
                    basket.pop()
                    count += 2
                    
            break
            
    return count
