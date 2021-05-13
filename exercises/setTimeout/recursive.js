

function printNums(n,i){
    if (n > 0){
        console.log(`${n}-${i} seconds`)
        setTimeout(function(delay){
            printNums(n-1,i+1)
        }, i * 1000)
    }
}

printNums(10,1)
