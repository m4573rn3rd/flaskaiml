function sendTimeToServer(){
    var time = new Date();
    var i = document.createElement("img");
    i.src = "/getTime?time=" + time;
    document.getElementById("time").innerHTML = time;
}