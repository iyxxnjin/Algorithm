function solution(intStrs, k, s, l) {
    let ret = []
    
    for(let i=0; i<intStrs.length; i++){
        const subStr = intStrs[i].substr(s, l);
        const num = Number(subStr);
        
        if(num > k){
            ret.push(num);
        }
    }
    return ret;
}