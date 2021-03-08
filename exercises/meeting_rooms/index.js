function minMeetingRooms (intervals){
    if (intervals.length <2){
        return intervals.length
    }

    intervals.sort((a,b) => a[0] - b[0])

    let roomsUsed = [intervals[0][1]]

    for (var i = 0; i < intervals.length ; i++){
        let [start,end] = [...intervals[i]]
        let earliest = Math.min(...roomsUsed)

        if (start<= earliest){
            roomsUsed.push(end)
        }else{
            roomsUsed[roomsUsed.indexOf(earliest)] = end
        }
    }
    return roomsUsed.length
}
