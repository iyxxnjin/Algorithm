function solution(n) {
    let arr = [];
    n_str = n.toString();
    
    for(let i=0; i<n_str.length; i++){
        arr.push(Number(n_str[i]));
    }
    
    return arr.reverse()

}