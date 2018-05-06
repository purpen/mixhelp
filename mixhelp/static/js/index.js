//    导航排他开始
$('.nav li>a').mouseenter(function(){
    $('.nav li>a').removeClass('active');
    $(this).addClass('active')
});

//左边问题点击事件
$('.issue>div>div').click(function(){

	$('.issue>div>div').parent().removeClass('issue-list');
    $(this).parent().addClass('issue-list');
    $('.issueTemp ul>li').removeClass('issueChange');
    $(this).siblings('ul li').addClass('issueChange')

	var subdivide = $('.issue>div>div>p').html()
	$('.issue-nav').html(subdivide)
	$('.issue-nav').attr('href', '/api/v1.0/index')

	if($(this).siblings("ul").css('display')=='none' ){

		$(this).siblings("ul").show();
		$(this).children('.TakeUp').show();
		$(this).children('.open').hide();
	}else{
		$(this).siblings("ul").hide();
		$(this).children('.TakeUp').hide();
		$(this).children('.open').show();
	}

	var id= $('.issue>div>div>p').attr('data-id')
	$.post('/main/index',{'id':id},function (data) {
		// alert(data)
    })

})
// //细节问题的点击事件
$('.issueTemp ul li a').click(function(){

    // var subdivide = $('.particular-issue ul li>a').html();
	// $('.particular-issue ul li>a').attr('href','/api/v1.0/info' + subdivide)
	$(this).parent('li').addClass('subdivide')
	var subdivide = $(this).attr('data-id');
    $('.issueTemp ul li a').attr('href','/main/issue_list/' + subdivide)
	var value = $(this).html()
	$('.subdivide-nav').html(value)
	$('.subdivide-nav').attr('href','/main/issue_list' + subdivide)

})

//详细问题点击事件
$('.particular-issue ul li a').click(function(){
	var num = $(this).attr('data-id');
	$('.particular-issue ul li>a').attr('href','/main/issue_info/' + num)
})
//
// window.onload=function(){
//
//
// 	}
// }



