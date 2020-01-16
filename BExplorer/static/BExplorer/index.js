console.log("zdarovenko");

$(document).ready(function(){

    $('#searchBlock').click(function(e) {  
        var inputvalue = $("#input").val();
        window.location.replace("http://127.0.0.1:8000/explorer/"+inputvalue);
    });
});

(function() {
	// sending a message
	$('#msgform').submit(async e => {
		e.preventDefault();
		console.log('message');

		var msg = $('#m').val();
		msg = msg //avoiding js injection
			.replace(/</g, '&lt;')
			.replace(/>/g, '&gt;')
			.trim();
		if (msg === '') return -1; //empty messages cannot be sent

		window.open("http://127.0.0.1:8000/explorer/" + msg,"_self")
	});
})();