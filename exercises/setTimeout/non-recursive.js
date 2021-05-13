let arr = []

for (let i = 10; i > 0; i--){
    arr.push(i)
}

function doSetTimeout(num,i){

    setTimeout(function (){
        console.log(`${num}-${i} seconds`)
    },i *1000)
}

arr.forEach((num,i)=>{
    doSetTimeout(num,i+1)
})
