function rotate(nums: number[], k: number): void {
    const N = nums.length;
    const K = k % N
    const B = N - K - 1;
    swap(nums, 0, B)
    swap(nums, B + 1, N - 1)
    swap(nums, 0, N - 1)
    
};
function swap(nums: number[], head: number, tail: number): void {
  while (head < tail) {
    let temp = nums[head]
    nums[head] = nums[tail]
    nums[tail] = temp
    head++;
    tail--;
  }
}
