function solution(my_string, is_suffix) {
    get_length = my_string.length - is_suffix.length
    
    if(my_string.slice(get_length) === is_suffix){
        return 1;
    }
    return 0;
}