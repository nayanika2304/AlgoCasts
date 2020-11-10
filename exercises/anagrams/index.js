// --- Directions
// Check to see if two provided strings are anagrams of eachother.
// One string is an anagram of another if it uses the same characters
// in the same quantity. Only consider characters, not spaces
// or punctuation.  Consider capital letters to be the same as lower case
// --- Examples
//   anagrams('rail safety', 'fairy tales') --> True
//   anagrams('RAIL! SAFETY!', 'fairy tales') --> True
//   anagrams('Hi there', 'Bye there') --> False

function createCharMap(str){
    let map = {}
    for(let char of str.replace(/[^\w]/g).toLowerCase()){
        map[char] = map[char] + 1 || 1
    }
    return map
}

function cleanString(str){
    return str.replace(/[^\w]/g,'').toLowerCase().split('').sort().join('');
}
function anagrams(stringA, stringB) {
    return cleanString(stringA) === cleanString(stringB)
}

module.exports = anagrams

/*
function anagrams(stringA, stringB) {
    let charMapA = createCharMap(stringA)
    let charMapB = createCharMap(stringB)

    if(Object.keys(charMapA).length !== Object.keys(charMapB).length){
        return false
    }
    Object.keys(charMapA).forEach(charA =>{
        if(charMapA[charA] !== charMapB[charA]){
            return false
        }
    })

    return true
}
 */
