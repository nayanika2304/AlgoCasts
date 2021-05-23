function greatestDifference(arr){

    // if there is only one element in the array
    if(arr.length <= 1){
        return -1
    }
    let currentMin = arr[0]
    let currentMaxDifference = 0

    for(let i = 0; i < arr.length; i++){
        if(arr[i] > currentMin && (arr[i] - currentMin > currentMaxDifference)){
            currentMaxDifference = arr[i] - currentMin
        }else if(arr[i] <= currentMin){
            currentMin = arr[i]
        }
    }

    if(currentMaxDifference <=0) return - 1

    return currentMaxDifference
}

console.log(greatestDifference([7, 8, 4, 9, 9, 15, 3, 1, 10]))
// should return the greatest difference of a-b such that a comes before b
