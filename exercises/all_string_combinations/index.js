function patterns(str, all) {

    // if the string is empty, return all the string sets
    if (str.length === 0) { return all; }

    // if character is 0 or 1 then add the character to each
    // string set we currently have so far
    if (str[0] === '0' || str[0] === '1') {
        for (var i = 0; i < all.length; i++) {
            all[i].push(str[0]);
        }
    }

    // for a wildcard, we make a copy of each string set
    // and for half of them we append a 0 to the string
    // and for the other half we append a 1 to the string
    if (str[0] === '?') {
        var len = all.length;
        for (var i = 0; i < len; i++) {
            var temp = all[i].slice(0);
            console.log(temp)
            all.push(temp);
        }

        for (var i = 0; i < all.length; i++) {
            (i < all.length/2) ? all[i].push('0') : all[i].push('1');
        }
    }

    // recursively calculate all string sets
    return patterns(str.substring(1), all);

}

console.log(patterns('10?1?', [[]]))
