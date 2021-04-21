function OverlappingRectangles(strArr) {

    // code goes here
    let coordinates = strArr[0].split('),(')
    coordinates[0] = coordinates[0].replace('(', '');
    coordinates[7] = coordinates[7].replace(')', '');
    coordinates = coordinates.map(function(el){
        return el.split(',').map(Number);
    });
    var r1 = coordinates.slice(0, 4).sort(function(a, b){
        return (a[0] + a[1]) - (b[0] + b[1]);
    })
    var r2 = coordinates.slice(4).sort(function(a, b){
        return (a[0] + a[1]) - (b[0] + b[1]);
    })


    let top1 = r1[3][1],
        bottom1 = r1[0][1],
        left1 = r1[0][0],
        right1 = r1[3][0],
        area1 = (top1 - bottom1) * (right1 - left1);

    let top2 = r2[3][1],
        bottom2 = r2[0][1],
        left2 = r2[0][0],
        right2 = r2[3][0];

    let overlapTop = Math.min(top1, top2),
        overlapBottom = Math.max(bottom1, bottom2),
        overlapRight = Math.min(right1, right2),
        overlapLeft = Math.max(left1, left2);
    overlapArea = (overlapTop - overlapBottom) * (overlapRight - overlapLeft);

    if(overlapTop < overlapBottom || overlapRight < overlapLeft || overlapArea === 0){
        return 0
    }
    return Math.floor(area1/overlapArea);
}

// keep this function call here
console.log(OverlappingRectangles(readline()));
