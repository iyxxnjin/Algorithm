function solution(a, b) {
    var answer = 0;
    let temp = (+(a.toString() + b.toString()))
    let mul_temp = 2*a*b
    
    return temp > mul_temp? temp : mul_temp
}