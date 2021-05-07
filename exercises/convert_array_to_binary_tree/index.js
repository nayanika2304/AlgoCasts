    function Node(val){
        this.val = val
        this.left = this.right = null
    }
    function convertBinaryTree(arr,root,i,n){
        if(i < n){
            root = new Node(arr[i])

            root.left = convertBinaryTree(arr,root.left,(2*i)+1,n)
            root.right = convertBinaryTree(arr,root.right,(2*i)+2,n)
        }

        return root
    }

    function BinaryTreeLCA(strArr) {
        let arr = strArr[0].replace(/[\[\]\s]/g, '').split(',');
        let arrLength = arr.length
        let n1 = strArr[1]
        let n2 = strArr[2]

        let root = convertBinaryTree(arr,null,0,arrLength)
        var lca = function(n){
            if(!n || n.val === n1 || n.val === n2){
                return n
            }
            var left = lca(n.left)
            var right = lca(n.right)

            if(!left){
                return right
            }
            if(!right){
                return left
            }
            return n.val
        }

        return lca(root)

    }
    BinaryTreeLCA(["[5, 2, 6, 1, 4, 8, 9]", "2", "6"]);
