function solution(my_string, index_list) {
    let word = '';
    for(let i=0; i<index_list.length; i++){
        word += my_string[index_list[i]]
    }
    return word;
}