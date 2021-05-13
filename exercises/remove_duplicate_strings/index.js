function removeDuplicates(str){
    const arr = str.split(' ')

    const set = new Set(arr)
    return [...set].join(' ')
}
