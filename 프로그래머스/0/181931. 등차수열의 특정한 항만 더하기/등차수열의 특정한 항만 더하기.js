function solution(a, d, included) {
    var answer = 0;
    
    for(i=0; i<included.length+1; i++) {
        if (included[i] == true) {
            answer += a + (i * d)
        }
    }
    return answer;
}