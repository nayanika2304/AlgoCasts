// Implement Function.prototype.bind

/*
const foo = function () {
    console.log(this.bar)
}

let baz = foo.bind({bar:'hello'})

baz()// Hello

*/

Function.prototype.bind = function (context){
    const fn = this
    return function (){
        fn.call(context)
    }
}
