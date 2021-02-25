// function fourSum(n){
//     for (int i = 0; i < n; ++i) {
//         // 'sums' hastable holds all possible sums a[k] + a[l]
//         // where k and l are both less than i
//
//         for (int j = i + 1; j < n; ++j) {
//             int current = a[i] + a[j];
//             int rest = X - current;
//             // Now we need to find if there're different numbers k and l
//             // such that a[k] + a[l] == rest and k < i and l < i
//             // but we have 'sums' hashtable prepared for that
//             if (sums[rest] != null) {
//                 // found it
//             }
//         }
//
//         // now let's put in 'sums' hashtable all possible sums
//         // a[i] + a[k] where k < i
//         for (int k = 0; k < i; ++k) {
//             sums[a[i] + a[k]] = pair(i, k);
//         }
//     }
// }
