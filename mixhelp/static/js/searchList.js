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

// 细节问题点击事件
$('.issueTemp ul li a').click(function(){

	var num = $(this).attr('data-id');
    $('.issueTemp ul li a').attr('href','/main/issue_list/' + num)

})

$('.particular-issue ul li a').click(function () {
	var num = $(this).attr('data-id');
	$('.particular-issue ul li a').attr('href', '/main/issue_info/' + num)

})




