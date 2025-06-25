function solution(my_string, is_prefix) {
    
    for(let i=0; i<is_prefix.length; i++){
        if(my_string.slice(0, is_prefix.length) === is_prefix){
            return 1
        }
        return 0
    }
}