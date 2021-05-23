// let arr = []
//
// for (let i = 10; i > 0; i--){
//     arr.push(i)
// }
//
// arr.forEach((num,i)=>{
//     setTimeout(function (){
//         console.log(`${num}-${i+1} seconds`)
//     },(i+1) *1000)
//
// })

function timer(n) {
    for (let i = 0; i < 10; i++) {
        setTimeout(function () {
            console.log(i);
        }, i * n);
    }
}

timer(2000);
