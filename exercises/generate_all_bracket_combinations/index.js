var all = [];

function parens(left, right, str) {

    // if no more brackets can be added then add the final balanced string
    if (left === 0 && right === 0) {
        all.push(str);
    }

    // if we have a left bracket left we add it
    if (left > 0) {
        parens(left-1, right+1, str+"(");
    }

    // if we have a right bracket left we add it
    if (right > 0) {
        parens(left, right-1, str+")");
    }

}

// the parameters parens(x, y, z) specify:
// x: left brackets to start adding
// y: right brackets we can add only after adding a left bracket
// z: the string so far
parens(3, 0, "");
console.log(all);
