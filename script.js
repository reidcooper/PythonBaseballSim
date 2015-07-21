$(document).ready(function(){
	var text = jquery.parseJson("description":"empty" || "first" || "second" || "third"|| "firstandsecond" || "secondandthird" || "firstandthird" || "loaded");
	$('input').click(function(){
		if (text.description == "first") {
			$(":1.jpeg").show();
		};
		else if (text.description == "second") {
			$.(":2.jpeg").show();
		};
		else if (text.description == "third") {
			$.(":3.jpeg").show();
		};
		else if(text.description == "empty"){
			$.(":empty.jpeg").show();
		}
		else if(text.description == "firstandsecond"){
			$.(":1and2.jpeg").show();
		}
		else if(text.description == "secondandthird"){
			$.(":2and3.jpeg").show();
		}
		else if(text.description == "firstandthird"){
			$.(":1and3.jpeg").show();
		}
		else if(text.description == "loaded"){
			$.(":loaded.jpeg").show();
		}
	});
	
});