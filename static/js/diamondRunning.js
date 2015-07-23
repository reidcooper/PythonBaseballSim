$(document).ready(function(){
	$(":1.jpeg").hide();
	$(":2.jpeg").hide();
	$(":3.jpeg").hide();
	$(":1and2.jpeg").hide();
	$(":1and3.jpeg").hide();
	$(":2and3.jpeg").hide();
	$(":loaded.jpeg").hide();
	$('input').click(function(){
	var text = jquery.parseJson("description":"100" || "010" || "001" || "000"|| "110" || "011" || "101" || "111");

		if (text.description == "100") {
			$(":1.jpeg").show();
		};
		else if (text.description == "010") {
			$.(":2.jpeg").show();
		};
		else if (text.description == "001") {
			$.(":3.jpeg").show();
		};
		else if(text.description == "000"){
			$.(":empty.jpeg").show();
		}
		else if(text.description == "110"){
			$.(":1and2.jpeg").show();
		}
		else if(text.description == "011"){
			$.(":2and3.jpeg").show();
		}
		else if(text.description == "101"){
			$.(":1and3.jpeg").show();
		}
		else if(text.description == "111"){
			$.(":loaded.jpeg").show();
		}
});
});
