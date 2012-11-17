function getLoop() {
	$.ajax({
		type: 'POST',
		url: 'http://131.123.87.121:8000/api/member/' + member_id + '/?format=json',
		datatype: 'jsonp',
		contentType: 'application/json',
		success: function(data) {
			console.log(data);
		}
	});
};