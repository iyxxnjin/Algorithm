function solution(rank, attendance) {
    let topRank = []
    
    for(let i=0; i<attendance.length; i++){
        if(attendance[i]) topRank.push([rank[i], i]);
    }
    
    topRank.sort((a,b) => a[0] - b[0]);

    let a = topRank[0][1]
    let b = topRank[1][1]
    let c = topRank[2][1]

    return 10000*a+100*b+c
}