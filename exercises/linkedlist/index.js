// --- Directions
// Implement classes Node and Linked Lists
// See 'directions' document

class Node {
    constructor(data,next = null) {
        this.data = data
        this.next = next
    }
}

class LinkedList {
    constructor() {
        this.head = null
    }

    insertFirst(data){
        this.head  = new Node(data,this.head)
    }

    size(){
        let size = 0

        if(!this.head){
            return size
        }
        while(this.head){
            this.head = this.head.next
            size+=1
        }

        return size
    }

    getFirst(){
        return this.head
    }

    getLast(){
        let node = this.head
        if(!node){
            return null
        }
        while(node){
            if(!node.next){
                return node
            }
            node = node.next
        }
    }

    clear(){
        this.head = null
    }
}

module.exports = { Node, LinkedList };
