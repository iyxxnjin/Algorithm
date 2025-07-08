function solution(myString) {
    const parts = myString.split("x");

    const result = [];
    for (let i = 0; i < parts.length; i++) {
        if (parts[i] !== "") {
            result.push(parts[i]);
        }
    }
    result.sort();
    return result;
}
