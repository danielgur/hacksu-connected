function getLoop() {
	$.ajax({
		type: 'GET',
		url: 'http://morning-earth-5099.herokuapp.com/api/member/'+ member_id + '/?format=jsonp',
		datatype: 'jsonp',
		contentType: 'application/jsonp',
		success: function(data) {
      alert(data);
		}
	});
};
