//
// Ajax Commands
//
var ajax_cmd;

if(window.XMLHttpRequest) {
  ajax_cmd = new XMLHttpRequest();
}
else {
  ajax_cmd = new ActiveXObject("Microsoft.XMLHTTP");
}

function servo_up() {
  ajax_cmd.open("POST","http://192.168.10.90:9977/servo_up",true);
  ajax_cmd.send();
}

function servo_down() {
  ajax_cmd.open("POST","http://192.168.10.90:9977/servo_down",true);
  ajax_cmd.send();
}
function servo_left() {
  ajax_cmd.open("POST","http://192.168.10.90:9977/servo_left",true);
  ajax_cmd.send();
}
function servo_right() {
  ajax_cmd.open("POST","http://192.168.10.90:9977/servo_right",true);
  ajax_cmd.send();
}


