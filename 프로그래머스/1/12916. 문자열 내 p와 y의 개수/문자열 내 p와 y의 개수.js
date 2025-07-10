function solution(s){
    let pCnt = 0;
    let yCnt = 0;
    
    s = s.toLowerCase();
    for(let i=0; i<s.length; i++){
        if(s[i] === 'p') pCnt += 1;
        if(s[i] === 'y') yCnt += 1;
    }
    
    if(pCnt === yCnt) return true;
    else return false;
}