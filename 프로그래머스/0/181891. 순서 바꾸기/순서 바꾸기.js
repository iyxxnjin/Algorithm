function solution(num_list, n) {
    let back = num_list.slice(n);
    let front = num_list.slice(0, n);
    
    return back.concat(front);
}
