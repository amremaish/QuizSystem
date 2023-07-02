function delete_object_modal() {
    var id = "delete_" + Math.floor(Math.random() * 1000);
    var modal = DeleteModal(id);
    $('#_modal').html(modal);
    $('#' + id).modal('toggle');
    $('#' + id).modal('show');
    return id;
}

function view_error_link_modal(msg, link, btn_text) {
    var id = "error" + Math.floor(Math.random() * 1000);
    var modal = ErrorModalLink(msg, id, link, btn_text);
    $('#_modal').html(modal);
    $('#' + id).modal('toggle');
    $('#' + id).modal('show');
}

function view_error_modal(msg) {
    var id = "error_" + Math.floor(Math.random() * 1000);
    var modal = ErrorModal(msg, id);
    $('#_modal').html(modal);
    $('#' + id).modal('toggle');
    $('#' + id).modal('show');
}

function view_info_modal(msg) {
    var id = "error_" + Math.floor(Math.random() * 1000);
    var modal = infoModal(msg, id);
    $('#_modal').html(modal);
    $('#' + id).modal('toggle');
    $('#' + id).modal('show');
}

function DeleteModal(modal_id) {
    var title = "info message"
    var msg = " Are you sure you want to delete this item ?";
    var close = "Close";
    var confirm = "Confirm"
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

function ErrorModal(msg, modal_id) {
    var title = "Error message"
    var close = "Close";
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
	            <button id = "btn_` + modal_id + `" onclick="$('#_modal').empty();$('.modal-backdrop').remove();" type="button" class="btn btn-danger" data-dismiss="modal">` + close + `</button>
	          </div>
	        </div>
	      </div>
	    </div>`;
}

function infoModal(msg, modal_id) {
    var title = "info message"
    var close = "Close";
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
	            <button id = "btn_` + modal_id + `" onclick="$('#_modal').empty();$('.modal-backdrop').remove();" type="button" class="btn btn-success" data-dismiss="modal">` + close + `</button>
	          </div>
	        </div>
	      </div>
	    </div>`;
}

function ErrorModalLink(msg, modal_id, link, btn_text) {
    var title = "Error message"
    return `    
	    <!-- Modal -->
	    <div class="modal fade" id="` + modal_id + `" tabindex="-1" role="dialog" aria-labelledby="exampleModalCenterTitle" aria-hidden="true">
	      <div class="modal-dialog modal-dialog-centered" role="document">
	        <div class="modal-content">
	          <div class="modal-header">
	            <h5 class="modal-title" id="exampleModalLongTitle">` + title + `</h5>
	            <button type="button" class="close" data-dismiss="modal" aria-label="Close">
	              <span aria-hidden="true">&times;</span>
	            </button>
	          </div>
	          <div class="modal-body">
	            ` + msg + `
	          </div>
	          <div class="modal-footer">
	             <a href = "` + link + `"class="btn btn-danger">` + btn_text + `</a>
	          </div>
	        </div>
	      </div>
	    </div>`;
}