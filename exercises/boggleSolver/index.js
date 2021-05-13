function BoggleSolver(strArr) {

                              // code goes here
        let words = strArr[1].split(',');
        let notFound = [];
        for(let i=0; i<words.length; i++) {
            let matrix = strArr[0].split(', ').map(x=> x.split(''));
        if (exist(matrix, words[i])) continue;
            notFound.push(words[i]);
        }
        if (notFound.length === 0 ) return true;
        else {
            return notFound.join(',')
        }
}

function exist(board, word) {
    const ROW_NUM = board.length, COL_NUM = board[0].length;


    for(let r=0; r < ROW_NUM; r++) {
        for(let c=0; c < COL_NUM; c++) {
            if(board[r][c] === word[0] && dfs(r,c,0)) return true;
        }
    }

    function dfs(r, c, idx) {
        if (word.length === idx) return true;
        if (r>=ROW_NUM || r < 0 || c>= COL_NUM || c<0 || board[r][c] !== word[idx]) {
            return false;
        }
        board[r][c] = '#' // mark as visited

        if (dfs(r+1, c, idx+1) || dfs(r-1, c, idx+1) || dfs(r, c+1, idx+1)
            || dfs(r,c-1, idx+1) || dfs(r+1, c+1, idx+1) || dfs(r-1, c-1, idx+1)
            || dfs(r+1, c-1, idx+1) || dfs(r-1, c+1, idx+1)
        ) return true;

        board[r][c] = word[idx]; // reset the word
    }

    return false;
}
// keep this function call here
console.log(BoggleSolver(readline()));
