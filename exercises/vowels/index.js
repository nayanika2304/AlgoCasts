// --- Directions
// Write a function that returns the number of vowels
// used in a string.  Vowels are the characters 'a', 'e'
// 'i', 'o', and 'u'.
// --- Examples
//   vowels('Hi There!') --> 3
//   vowels('Why do you ask?') --> 4
//   vowels('Why?') --> 0

function vowels(str) {
    //g : don`t stop at the first match, go on
    //i : case insensitive
    const matches = str.match(/[aeiou]/gi)

    return matches ? matches.length : 0

}

module.exports = vowels;

/*
function vowels(str) {
    const vowels = ['a','e','i','o','u']
    let count = 0
    return str.split('').reduce((a, c) => {
        if (vowels.includes(c.toLowerCase())) {
            count += 1
        }
        a = count
        return a
    }, 0)
}
 */
