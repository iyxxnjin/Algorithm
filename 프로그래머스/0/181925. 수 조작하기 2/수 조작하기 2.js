function solution(numLog) {
    const orders = { 1:'w', '-1':'s', 10:'d', '-10':'a'};
    let result = '';
    
    for (let i=1; i<numLog.length; i++){
        let order = numLog[i] - numLog[i-1];
        result += orders[order];
    }
    return result
}