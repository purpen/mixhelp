//    导航排他开始
$('.nav li>a').mouseenter(function(){
    $('.nav li>a').removeClass('active');
    $(this).addClass('active')
});

//左边问题点击事件
$('.issue>div>div').click(function(){
	
	if($(this).siblings("ul").css('display')=='none' || $('.particular-issue ul>li>a').html()){
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

	var subdivide = $('.issue>div>div>p').html()
	$('.issue-nav').html(subdivide)
	$('.issue-nav').attr('href', '/api/v1.0/index')

	
})
// //细节问题的点击事件
$('.issueTemp ul li a').click(function(){

    // var subdivide = $('.particular-issue ul li>a').html();
	// $('.particular-issue ul li>a').attr('href','/api/v1.0/info' + subdivide)
	$(this).parent('li').addClass('subdivide')
	var subdivide = $(this).html();
    $('.issueTemp ul li a').attr('href','/api/v1.0/list/' + subdivide)
	$('.subdivide-nav').html(subdivide)
	$('.subdivide-nav').attr('href','/api/v1.0/list' + subdivide)


	

})

//详细问题点击事件
$('.particular-issue ul li a').click(function(){
	var subdivide = $(this).html();
	$('.particular-issue ul li>a').attr('href','/api/v1.0/info/' + subdivide)
})
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




