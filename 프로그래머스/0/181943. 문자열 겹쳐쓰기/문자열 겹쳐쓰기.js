function solution(my_string, overwrite_string, s) {
    let answer = '';
    
    for(let i = 0; i < my_string.length; i++) {
        if(i >= s && i < s + overwrite_string.length) {
            answer += overwrite_string[i-s];
        }
        else {
            answer += my_string[i];
        }
    }
    return answer;
}
