function solution(x) {
    let str_x = x.toString();
    let sum = 0;
    
    for(let i=0; i<str_x.length; i++){
        sum += Number(str_x[i]);
    }

    return x % sum ? false : true
}