function solution(arr1, arr2) {
    if (arr1.length !== arr2.length) {
        return arr1.length > arr2.length ? 1 : -1;
    }
    
    let sum_arr1 = 0;
    let sum_arr2 = 0;
    
    for (let i = 0; i < arr1.length; i++) {
        sum_arr1 += arr1[i];
        sum_arr2 += arr2[i];
    }
    
    if (sum_arr1 === sum_arr2) return 0;
    return sum_arr1 > sum_arr2 ? 1 : -1;
}
