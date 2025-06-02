def solution(survey, choices):
    score = [3,2,1,0,1,2,3]
    type_dict = {"R":0, "T":0, "C":0, "F":0, "J":0, "M":0, "A":0, "N":0}

    for i in range(len(survey)):
        type1, type2 = survey[i][0], survey[i][1]
        choice = choices[i]
        if choice <= 3:
            type_dict[type1] += score[choice-1]
                
        elif choice >= 5:
            type_dict[type2] += score[choice-1]
                
    sets = [("R", "T"), ("C", "F"), ("J", "M"), ("A", "N")]
    result =""
    
    for type1, type2 in sets:
        if type_dict[type1] > type_dict[type2]:
            result += type1
            
        elif type_dict[type1] < type_dict[type2]:
            result += type2
            
        else:
            result += min(type1, type2)
            
    return result
    