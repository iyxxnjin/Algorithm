function solution(num_list) {
    let even_num = ''
    let odd_num = ''
    
    for(let i=0; i<num_list.length; i++) {
        if (num_list[i] % 2 == 0) {
            even_num += num_list[i]
        }
        else {
            odd_num += num_list[i]
        }
    }
    return Number(even_num) + Number(odd_num)
}