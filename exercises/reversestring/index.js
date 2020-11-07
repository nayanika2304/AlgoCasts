// --- Directions
// Given a string, return a new string with the reversed
// order of characters
// --- Examples
//   reverse('apple') === 'leppa'
//   reverse('hello') === 'olleh'
//   reverse('Greetings!') === '!sgniteerG'

//apple
function reverse(str) {
    return str.split('').reduce((rev,char) => char + rev,'')
}

//other solutions ----
/*
const arr = str.split('')
arr.reverse()
arr.join('')
 */

/*for(let i = str.length - 1;i >= 0;i--){
        reverse += str[i]
}*/

/*
for (let character of str){
        reverse = character + reverse
    }
 */



module.exports = reverse;
