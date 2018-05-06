//    导航排他开始
$('.nav li>a').mouseenter(function(){
    $('.nav li>a').removeClass('active');
    $(this).addClass('active')
});
// window.onload=function(){
// 	  if($('.particular-issue ul>li>a').html()){
// 		$('.issue>div>div').siblings("ul").eq($('.particular-issue ul').index()).show();
// 		$('.issueTemp div .TakeUp').show();
// 		$('.issueTemp div .open').hide();
// 		}
// }

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

	var subdivide = $('.issue>div>div>p').html()
	$('.issue-nav').html(subdivide)
	$('.issue-nav').attr('href', '/api/v1.0/index')

	
})
// //细节问题的点击事件
$('.issueTemp ul li a').click(function(){

    // var subdivide = $('.particular-issue ul li>a').html();
	// $('.particular-issue ul li>a').attr('href','/api/v1.0/info' + subdivide)
	$(this).parent('li').addClass('subdivide')
	var num = $(this).attr('data-id')
    $('.issueTemp ul li a').attr('href','/main/issue_list/' + num)
	$('.subdivide-nav').attr('href','/main/issue_list' + num)

})

//详细问题点击事件
$('.particular-issue ul li a').click(function(){
	var subdivide = $(this).html();
	var num = $(this).attr('data-id')
	$('.particular-issue ul li>a').attr('href','/main/issue_info/' + num)
})





