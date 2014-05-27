$(function(){
		$("#more").click(function(){
			var q=$("#more_query").val();
			var s=$("#more_size").val();
			var	o=$("#more_offset").val();
			if (s == "")
			{
				s=500
			}
			$("html, body").animate({ scrollTop: 0 }, "slow");
			$('.theContent').fadeOut('slow',function(){
			$('.theContent').empty();
			$.get("/",{query:q,size:s,offset:o,refresh:"yes"},function(result){
				$('.theContent').append(result);			
				$('#result').empty();
				$('#result').append(q);
				$('#result').append(" gifs under ");
				$('#result').append(s);
				$('#result').append(" kb");
				$('.theContent').fadeIn('slow');
			});
			console.log("MORE!");

			})
		});
	})