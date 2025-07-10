function solution(n) {
    let num_n = 0;
    
    str_n = n.toString()
    
    for(let i=0; i<str_n.length; i++){
        num_n += Number(str_n[i]);
    }
    
    return num_n;
}