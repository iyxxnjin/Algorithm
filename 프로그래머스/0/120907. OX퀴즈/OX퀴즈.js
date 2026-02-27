function solution(quiz) {
    return quiz.map((q) => {
        const [X, operator, Y, equal, Z] = q.split(" ");
        
        let calc = 0;
        
        if(operator === "+"){
            calc = Number(X) + Number(Y);
        } else calc = Number(X) - Number(Y);
        
        return calc === Number(Z) ? "O" : "X";
    })
}