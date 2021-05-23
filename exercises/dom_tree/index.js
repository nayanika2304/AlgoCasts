/*
We have two identical dom trees A and B. For DOM tree A, we have the location of an element
Create a function to find the same element in tree
 */
function reversePath(element,root){
    const path = []
    let pointer = element
    while (pointer.parent){
        const index = pointer.parent.children.indexOf(pointer)
        path.push(index)
        pointer = pointer.parent
    }

    pointer = root

    while(path.length){
        pointer = pointer.parent.children[path.pop()]
    }

}
