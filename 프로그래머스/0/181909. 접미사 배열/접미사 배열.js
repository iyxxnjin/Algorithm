function solution(my_string) {
    let result = [];
    
    for(let i=0; i<my_string.length; i++){
        let char = my_string.slice(i);
        result.push(char);
    }
    
    result.sort();
    return result;
}