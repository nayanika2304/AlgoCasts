var findKthLargest = function(nums, k) {
    return nums.sort(function(a,b) { return b-a })[k-1];
}

console.log(findKthLargest([12,3,4,567,342],3))
