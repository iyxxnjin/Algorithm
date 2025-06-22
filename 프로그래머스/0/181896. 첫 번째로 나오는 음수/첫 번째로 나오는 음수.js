function solution(num_list) {
    for(let i=0; i<num_list.length; i++){
        if(num_list[i].toString().includes('-')) {
            return i;
        }
    }
    return -1;
}