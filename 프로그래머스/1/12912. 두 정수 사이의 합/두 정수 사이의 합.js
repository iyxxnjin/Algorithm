function solution(a, b) {
    if(a > b) { const tmp = a; a = b; b = tmp; }
    
    let sum = 0;
    
    for(let i=a; i<=b; i++){
        sum += i;
    }
    
    return sum;
}