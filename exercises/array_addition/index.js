function ArrayAddition(arr) {

    // code goes here
    const largest = arr.sort((a,b) => a-b).pop()

    var sets = [[]]
    for (let i = 0 ; i < arr.length; i++){
        for (let j = 0, len = sets.length; j< len;j++){
            var temp = sets[j].concat(arr[i])

            var s = temp.reduce(function(p, c) { return p + c; });
            if (s === largest) { return "true"; }
        }
    }
    return false

}

// keep this function call here
console.log(ArrayAddition());
