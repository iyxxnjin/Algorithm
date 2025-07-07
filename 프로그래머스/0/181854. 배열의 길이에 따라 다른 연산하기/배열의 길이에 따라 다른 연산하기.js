function solution(arr, n) {
  const odd = arr.length % 2 === 1;

  return arr.map((value, index) => {
    if (odd && index % 2 === 0) {
      return value + n;
        
    } else if (!odd && index % 2 === 1) {
      return value + n;
    }
      
    return value; 
  });
}
