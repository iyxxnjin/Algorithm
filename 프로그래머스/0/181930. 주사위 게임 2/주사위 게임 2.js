function solution(a, b, c) {
    let result = 0
    let 합 = a + b + c
    let 제곱 = a*a + b*b + c*c
    let 세제곱 = a**3 + b**3 + c**3
    
    if (a === b && b === c){
        result = 합 * 제곱 * 세제곱
    }
    else if (a === b || b === c || c === a) {
        result = 합 * 제곱
    }
    else {
        result = 합
    }
    
    return result
}