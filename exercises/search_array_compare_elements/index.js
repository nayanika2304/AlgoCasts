function search(arr){
    const hash = arr.reduce((a,c) =>{
        a[c] = arr.filter(item => c !== item)
        return a
    },{})

    let res = []

    Object.keys(hash).forEach((key, i) => {
        hash[key].forEach((item, j) => {
            if (item[j].indexOf(key[j]) !== -1 && res.length === 0) {
                 res = [i, hash[key].indexOf(item) + 1, j]
            }

        })
    })

    return res
}

console.log(search(['abc','cab','dbe']))
