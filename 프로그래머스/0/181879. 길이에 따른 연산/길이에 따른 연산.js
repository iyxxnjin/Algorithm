function solution(num_list) {
    let mul = 1
    let sum = 0
    
    if (num_list.length <= 10){
        for(i=0; i<num_list.length; i++){
            mul *= num_list[i]
        }
        return mul
    }
    else {
        for(i=0; i<num_list.length; i++){
            sum += num_list[i]
        }
        return sum
    }
    
}