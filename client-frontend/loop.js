function getLoop() {
	$.ajax({
		type: 'GET',
		url: 'http://morning-earth-5099.herokuapp.com/api/member/'+ member_id + '/?callback=mycallback',
		datatype: 'jsonp',
		contentType: 'application/json',
		success: function(data) {
      alert(data);
		}
	});
};

mycallback = function(data){
  alert(data);
};
