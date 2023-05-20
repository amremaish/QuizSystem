var web = {
   "server": "http://127.0.0.1:8000"
};

function checkTokenExistance(){
	if  (readCookie('token') == ''){
		var modal = ErrorModal("invalid authentication please login again" , "error_modal");
		$('#_modal').html(modal);
		$('#error_modal').modal('toggle');
		$('#error_modal').modal('show');
	    $("#btn_error_modal").click(function(e) {
	    		window.location="/admin/login";
	    });

		return false ;
	}

	return true ;
}

function writeCookie(name,value) {
    var date, expires , days = 99999;
    if (days) {
        date = new Date();
        date.setTime(date.getTime()+(days*24*60*60*1000));
        expires = "; expires=" + date.toGMTString();
            }else{
        expires = "";
    }
    document.cookie = name + "=" + value + expires + "; path=/";
}


function readCookie(name) {
    var i, c, ca, nameEQ = name + "=";
    ca = document.cookie.split(';');
    for(i=0;i < ca.length;i++) {
        c = ca[i];
        while (c.charAt(0)==' ') {
            c = c.substring(1,c.length);
        }
        if (c.indexOf(nameEQ) == 0) {
            return c.substring(nameEQ.length,c.length);
        }
    }
    return '';
}