function CoinDeterminer(num) {

    // Each memo[i] is the least amount of coins
    // that can make the value equal to the index value.
    const coins = [1,5,7,9,11]
    let amount = num
    const memo = Array(amount + 1).fill(Infinity);
    memo[0] = 0;

    for (let i = 1; i <= amount; i++) {
        for (const coin of coins) {
            if (i - coin >= 0) {
                memo[i] = Math.min(memo[i - coin] + 1,memo[i]);
            }
        }
    }
    return memo[amount] === Infinity ? -1 : memo[amount];

}

// keep this function call here
console.log(CoinDeterminer(readline()));
