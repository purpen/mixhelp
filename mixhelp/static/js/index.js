//    导航排他开始
$('.nav li>a').mouseenter(function(){
    $('.nav li>a').removeClass('active');
    $(this).addClass('active')
});

//左边问题点击事件
$('.issue>div>div').click(function(){
	
	if($(this).siblings("ul").css('display')=='none'){
		// $('.result .issue-nav').html($(this).children('p').html())
		$(this).siblings("ul").show();
		$('.issueTemp div .TakeUp').show();
		$('.issueTemp div .open').hide();
	}else{
		$(this).siblings("ul").hide();
		$('.issueTemp div .TakeUp').hide();
		$('.issueTemp div .open').show();
	}

	var issue = $(this).children('p').html();
	
	
})
// //细节问题的点击事件
$('.issueTemp ul li a').click(function(){
    $(this).attr('href','')
    var subdivide = $(this).html();
	$('.particular-issue ul li>a').attr('href','subdivide')
	$(this).parent('li').addClass('subdivide')
	

})

//详细问题点击事件
// $('.particular-issue ul>li').click(function(){
// 	// $('.result .crumbs1').show();
// 	// $('.particular-nav').html($(this).children('a').html())
// 	// $('.particular-issue').hide();
// 	// $('.particular').show();
// 	// 详细问题标题事件
//     $('.particular h3').html($(this).html())


//     var particular = $(this).html();
// 	console.log(particular)
	
// 	// $.get(#?particular=particular,function(data){
// 	// 	console.log(data)
// 	// })
// })




