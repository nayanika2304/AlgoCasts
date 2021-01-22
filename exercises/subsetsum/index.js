// Find subset of a, of length e, that sums to n
function subset_sum(a, e, n) {
    if (n < 0)   return null;           // Nothing adds up to a negative number
    if (e === 0) return n === 0 ? [] : null; // Empty list is the solution for a target of 0

    a = a.slice();
    while (a.length) {              // Try remaining values
        var v = a.shift();            // Take next value
        var s = subset_sum(a, e - 1, n - v); // Find solution recursively
        if (s) return s.concat(v);    // If solution, return
    }
}
