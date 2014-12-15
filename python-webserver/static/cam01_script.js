
//
// MJPEG
//
var mjpeg_img;
var is_armed;

function reload_img() {
  mjpeg_img.src = "http://192.168.10.90:80/cam_pic.php?time=" + new Date().getTime();
}

function error_img() {
  setTimeout("mjpeg_img.src = 'http://192.168.10.90:80/cam_pic.php?time=' + new Date().getTime();", 100);
}




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

function is_armed() {
  ajax_cmd.onreadystatechange=function()
  {
  if (ajax_cmd.readyState==4 && ajax_cmd.status==200)
    {
      document.getElementById("isArmed").innerHTML = ajax_cmd.responseText;
    }
  }
  ajax_cmd.open("POST","http://192.168.10.90:9977/is_armed",true);
  ajax_cmd.send();
}



//
// Init
//
function init() {

  // mjpeg
  mjpeg_img = document.getElementById("mjpeg_dest");
  mjpeg_img.onload = reload_img;
  mjpeg_img.onerror = error_img;
  reload_img();

  //Status
  is_armed();
 
}
