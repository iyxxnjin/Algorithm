function solution(a, b) {
    var answer = 0;
    let temp = (+(a.toString() + b.toString()))
    let mul_temp = 2*a*b
    
    if (temp > mul_temp){
        answer = temp
    }
    else {
        answer = mul_temp
    }
    return answer;
}