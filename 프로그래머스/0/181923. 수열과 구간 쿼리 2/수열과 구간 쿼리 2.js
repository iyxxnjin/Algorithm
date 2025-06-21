function solution(arr, queries) {
    let result = [];
    
    for (let [s,e,k] of queries) {
        let min = Infinity;
        
        for (let j=s; j<=e; j++) {
            if(arr[j] > k && arr[j] < min) {
                min = arr[j];
            }
        }
        result.push(min == Infinity ? -1 : min);
    }
    return result;
}