function insertInterval(arr, interval) {

    var newSet = [];
    var endSet = [];
    var i = 0;

    // add intervals that come before the new interval
    while (i < arr.length && arr[i][1] < interval[0]) {
        newSet.push(arr[i]);
        i++;
    }

    // add our new interval to this final list
    newSet.push(interval);

    // check each interval that comes after the new interval to determine if we can merge
    // if no merges are required then populate a list of the remaining intervals
    while (i < arr.length) {

        var last = newSet[newSet.length - 1];
        if (arr[i][0] < last[1]) {
            var newInterval = [Math.min.apply(null, [last[0], arr[i][0]]), Math.max.apply(null, [last[1], arr[i][1]])];
            newSet[newSet.length - 1] = newInterval;

        } else {
            endSet.push(arr[i]);
        }
        i++;
    }

    return newSet.concat(endSet);

}

console.log(insertInterval([[1,5],[10,15],[20,25]], [12,27]))
