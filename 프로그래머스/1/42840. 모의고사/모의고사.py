def solution(answers):
    giveup1 = [1,2,3,4,5]
    giveup2 = [2,1,2,3,2,4,2,5]
    giveup3 = [3,3,1,1,2,2,4,4,5,5]
    
    guesses = [giveup1, giveup2, giveup3]
    count = [0, 0, 0]
    
    for i in range(len(answers)):
        for j, guess in enumerate(guesses):
            if answers[i] == guess[i % len(guess)]:
                count[j] += 1
    
    max_count = max(count)
    
    return [i+1 for i, c in enumerate(count) if c == max_count]
            
            
            
    