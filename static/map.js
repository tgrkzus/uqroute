function generate_map(){
	$.getJSON($SCRIPT_ROOT + '/_display_map', {
	}, function(data) {
	$("#test").text(JSON.stringify(data.result));
	});
	return false
};
