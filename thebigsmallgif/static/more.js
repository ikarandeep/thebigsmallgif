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
			var qdash=q.replace(/\s+/g, '-').toLowerCase();
			var url="query=" + qdash + "&size=" + s + "&offset=" + o;
			console.log("?query=" + qdash + "&size=" + s + "&offset=" + o)
			$.get("/",{query:qdash,size:s,offset:o,refresh:"yes"},function(result){
				$('.theContent').append(result);			
				$('#result').empty();
				$('#result').append(q);
				$('#result').append(" gifs under ");
				$('#result').append(s);
				$('#result').append(" kb");
				$('#url-goes-here').empty();
				$('#url-goes-here').append('<a href="?' + url + '">' + url + '</a>');
				$('.theContent').fadeIn('slow');
			});
			console.log("MORE!");

			})
		});
	})