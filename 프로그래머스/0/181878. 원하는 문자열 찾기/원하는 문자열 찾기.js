function solution(myString, pat) {
    let my_String = myString.toLowerCase()
    let my_pat = pat.toLowerCase()
    
    return my_String.includes(my_pat)? 1 : 0
    
}