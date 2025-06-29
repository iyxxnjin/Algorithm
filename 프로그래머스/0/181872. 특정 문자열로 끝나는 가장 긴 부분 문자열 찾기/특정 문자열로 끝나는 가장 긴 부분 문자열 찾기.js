function solution(myString, pat) {
    let answer = '';
    
    for(let i=0; i<myString.length; i++){
        let part = myString.slice(0, myString.length - i);
        
        if (part.endsWith(pat)){
            answer = part;
            break;
        }
    }
    return answer;
}