let arr = []

for (let i = 10; i > 0; i--){
    arr.push(i)
}

function doSetTimeout(num,i){
    setTimeout(function (delay){console.log(`${num}-${delay/1000} seconds`)},i *1000,i*1000)
}

arr.forEach((item,i)=>{
    doSetTimeout(item,i+1)
})
