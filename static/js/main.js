var socket = io();
socket.on('message', function(message) {
    let div = document.getElementById('messages');
    let new_message = document.createElement('h4');
    new_message.innerHTML = message;
    div.append(new_message);
});

document.onkeydown = function (e) {
  e = e || window.event;
  switch (e.which || e.keyCode) {
        case 13 :
            send_message();
  }
}

function send_message() {
    var now = new Date();
    var time = now.getHours() + ":" + now.getMinutes() + ":" + now.getSeconds();
    time += "-" + now.getDate() + "." + now.getMonth() + "." + now.getFullYear() + " : ";
    var val = document.getElementById('tx').value;
    if (val) {
        socket.send(time + val);
        document.getElementById("tx").value = "";
    }
}