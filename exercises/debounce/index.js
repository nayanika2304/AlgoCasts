// to fire something when a person has stopped typing

function debounce(fn,time){
    let setTimeoutId
    return function(){
        if (setTimeoutId){
            clearTimeout(setTimeoutId) // debounce
            //return; // throttle
        }
        setTimeoutId = setTimeout(() =>{
            fn.apply(this,arguments);
            setTimeoutId = null
        },time)
    }
}
