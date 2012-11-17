function getLoop() {
  alert("made it");
	$.ajax({
		type: 'GET',
		url: 'http://131.123.87.121:8000/api/member/' + member_id + '/?format=jsonp',
		datatype: 'json',
		contentType: 'application/json',
		success: function(data) {
      alert(data);
		}
	});
};
