//    导航排他开始
$('.nav li>a').mouseenter(function(){
    $('.nav li>a').removeClass('active');
    $(this).addClass('active')
});

//左边问题点击事件
$('.issue>div>div').click(function(){
	
	if($(this).siblings("ul").css('display')=='none'){
		$(this).siblings("ul").show();
		$('.issueTemp div .TakeUp').show();
		$('.issueTemp div .open').hide();
	}else{
		$(this).siblings("ul").hide();
		$('.issueTemp div .TakeUp').hide();
		$('.issueTemp div .open').show();
	}

})
//搜索点击事件
// $('.btn').click(function(){
// 	if($('.search input').val()){
// 		$('.result').hide();
// 		$('.search-content').show();
// 	}else{
// 		$('.result').hide();
// 		$('.search-content').hide();
// 	}


//     var searchVal = $('.search input').val()
// 	console.log(searchVal)

	// $.get(#?searchVal=searchVal,function(data){
		// if(data.length<1){
		// 	$('.search-val').html(searchVal)
		// }
	// 	console.log(data)
	// })
	
// })
