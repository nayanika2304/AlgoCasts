function mergeAppointments(appointments, properties) {
    let objProperties = properties.reduce((a,c) => {
        let arr = c.split(',')
        a[arr[0]] = arr[1] || null
        return a
    },{})


    let result = appointments.map(appointment => {
        let appointmentArr = appointment.split(',')
        const index = appointmentArr.findIndex(d => d === appointmentArr[2])
        if(objProperties[appointmentArr[index]]){
            appointmentArr[index] = objProperties[appointmentArr[2]]
            return appointmentArr.join(',')
        }
    })
    return result
}




mergeAppointments([
    "A1,2019-03-01,P1",
    "A2,2019-01-04,P2",
    "A3,2019-05-10,P1",
    "A4,2019-05-10,P3"
],[
    "P1,22 Yonge St",
    "P2,471 Richmond St W"
])
/*
let Output:
    [
        "A1,2019-03-01,22 Yonge St",
        "A2,2019-01-04,471 Richmond St W",
        "A3,2019-05-10,22 Yonge St",
    ]

 */
