
function startInterval(h,m,s,startTimer,time,id,hid){

        startTimer = setInterval(function() {

            console.log(1);
            if(hid.value!=0){
            console.log(2);
            time = timer(h,m,s,time);}
            else{
             console.log(3);
                h.value = 0;
                m.value= 0;
                s.value = 0;
                clearInterval(startTimer);
                return;
            }
        }, 1000);
    }


function timer(h,m,s,time){

    const minutes = Math.floor((time%3600)/60);
    let seconds = (time%3600)%60;
    const hour = Math.floor(time /3600)
    seconds = seconds < 10 ? '0' + seconds : seconds;
    h.value =hour;
    m.value = minutes;
    s.value = seconds;
    time++;
    return time;
}

// //stop the function after pressing the reset button, 
// //so the time wont go down when selecting a new time after pressing reset
function stopInterval() {
    h.value = 0;
    m.value= 0;
    s.value = 0;
    clearInterval(startTimer);
}

function start_timer(id,user_id){
   /* console.log(id);*/
    //var start = document.getElementById('start-'+id);
    //var reset = document.getElementById('reset-'+id);

    var startTimer = 0;
    var startingMin = 0;
    var time = startingMin*60;

    var h = document.getElementById("hour-"+ id);
    var m = document.getElementById("minute-"+id);
    var s = document.getElementById("sec-"+id);
    var hid= document.getElementById("hid-"+id);
    hid.value=1;
    console.log('start');
    fetch('http://52.172.183.85:8080/task/start/',{
        method:'POST',
        headers:{
           'Content-Type': 'application/json',
        },
        body:JSON.stringify({
            user_id:user_id,
            task_id:id,
        })
    }).then(res => {
        return res.json()
    })
    .then(data=>hid.value=data['time_entry_id'])
    .catch(error=>console.log(error))
    console.log('end');


    

    //store a reference to the startTimer variable
   
    startInterval(h,m,s,startTimer,time,id,hid);


}

function stop_timer(id,user_id){


    var h = document.getElementById("hour-"+ id);
    var m = document.getElementById("minute-"+id);
    var s = document.getElementById("sec-"+id);
    var hid = document.getElementById("hid-"+id);
    console.log("start");
    fetch('http://52.172.183.85:8080/task/end/',{
        method:'POST',
        headers:{
            'Content-Type':'application/json'
        },
        body:JSON.stringify({
            hour:h.value,
            minute:m.value,
            second:s.value,
            user_id:user_id,
            task_id:id,
            time_entry_id:hid.value,
        })
    }).then(res => {
        return res.json()
    })
    .then(data=>console.log(data))
    .catch(error=>console.log(error))
    console.log('end');
    

    h.value=0;
    m.value=0;
    s.value=0;
    hid.value=0;
}