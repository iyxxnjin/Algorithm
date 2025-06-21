function solution(l, r) {
    let result = [];
    
    for (let i=l; i<=r; i++) {
        let string_i = i.toString();
        
        if ([...string_i].every(ch => ch =='0' || ch =='5')) {
            result.push(Number(string_i));
        }
    }
    return result.length > 0 ? result : [-1]
}