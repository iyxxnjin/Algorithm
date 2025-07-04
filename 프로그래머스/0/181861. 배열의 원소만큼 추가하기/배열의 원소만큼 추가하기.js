function solution(arr) {
    let result = [];

    for (let i = 0; i < arr.length; i++) {
        let value = arr[i];
        for (let j = 0; j < value; j++) {
            result.push(value);
        }
    }

    return result;
}
