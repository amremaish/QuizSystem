function delete_object_modal() {
    var id = "delete_" + Math.floor(Math.random() * 1000);
    var modal = DeleteModal(id);
    $('#_modal').html(modal);
    $('#' + id).modal('toggle');
    $('#' + id).modal('show');
    return id;
}

function DeleteModal(modal_id) {
    var title = "info message"
    var msg = " Are you sure you want to delete this item ?";
    var close = "Close";
    var confirm = "Confirm"
    // if (readCookie("lang") == "ar"){
    //     title = "رسالة تنبية";
    //     msg = "هل انت متأكد بأنك تريد حذف هذا العنصر ؟";
    // 	close ="إغلاق";
    // 	confirm = "تأكيد";
    // }
    return `    
	    <!-- Modal -->
	    <div class="modal fade" id="` + modal_id + `" tabindex="-1" role="dialog" aria-labelledby="exampleModalCenterTitle" aria-hidden="true">
	      <div class="modal-dialog modal-dialog-centered" role="document">
	        <div class="modal-content">
	          <div class="modal-header">
	            <h5 class="modal-title" id="exampleModalLongTitle">` + title + `</h5>
	          </div>
	          <div class="modal-body">
	            ` + msg + `
	          </div>
	          <div class="modal-footer">
		            <button id= "confirm_` + modal_id + `" class="btn btn-danger">` + confirm + `</button>
	          </div>
	        </div>
	      </div>
	    </div>`;
}