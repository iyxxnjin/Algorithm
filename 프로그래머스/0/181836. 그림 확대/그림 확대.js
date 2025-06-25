function solution(picture, k) {
    let result = [];
    
    for(let i=0; i<picture.length; i++){
        const sep_picture = picture[i].split('');
        
        let k_multi = ''
        for(let c of sep_picture){
            k_multi += c.repeat(k);
        }
        
        for(let j=0; j<k; j++){
            result.push(k_multi);
        }
    }
    
    return result;
}