function myPow(x: number, n: number): number {
  let result = 1;
  for (let i = 0; i < Math.abs(n); i++) {
    result *= x;
  }
  return n < 0 ? 1 / result : result;
};
