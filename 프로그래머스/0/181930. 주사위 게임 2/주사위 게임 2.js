function solution(a, b, c) {
    let result = 0
    let 합 = a+b+c
    let 제곱 = a*a+b*b+c*c
    let 세제곱 = a*a*a+b*b*b+c*c*c
    
    if (a == b && b == c){
        result = 합*제곱*세제곱
    }
    else if (a != b && a != c && b != c) {
        result = 합
    }
    else {
        result = 합*제곱
    }
    
    return result
}