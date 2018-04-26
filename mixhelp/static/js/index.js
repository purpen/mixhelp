//    导航排他开始
$('.nav li>a').mouseenter(function(){
    $('.nav li>a').removeClass('active');
    $(this).addClass('active')
});

//左边问题点击事件
$('.issue>div>div').click(function(){

	if($(this).siblings("ul").css('display')=='none'){
		$('.result .issue-nav').html($(this).children('p').html())
		$(this).siblings("ul").show();
		$('.issueTemp div .TakeUp').show();
		$('.issueTemp div .open').hide();
	}else{
		$('.issueTemp ul').hide();
		$('.issueTemp div .TakeUp').hide();
		$('.issueTemp div .open').show();
	}

	var issue = $(this).children('p').html();

	// $.get('/index/subdivide',function(data){
	// 	console.log(data)
	// })
	
	
})
//细节问题的点击事件
$('.issueTemp ul li').click(function(){
	 $('.result').show();
	 $('.search-content').hide();
	 $('.search-failure').hide();
	 $('.result .crumbs').show();
	 $('.result .crumbs1').hide();
	 $('.subdivide-nav').html($(this).html())
	 $('.particular-nav').html('')
	 $('.particular').hide();
	 $('.issueTemp ul li').removeClass('subdivide');
    $(this).addClass('subdivide');
    $('.particular-issue').show();
    var idx = $(this).index();
    //让内容框的第 idx 个显示出来，其他的被隐藏
    $(".result>div>ul").eq(idx).show().siblings().hide();

	// var subdivide = $(this).html();
	// console.log(subdivide)

	// $.get(#?subdivide=subdivide,function(data){
	// 	console.log(data)
	// })
})

//详细问题点击事件
$('.particular-issue ul>li').click(function(){
	$('.result .crumbs1').show();
	$('.particular-nav').html($(this).html())
	$('.particular-issue').hide();
	$('.particular').show();
	// 详细问题标题事件
    $('.particular h3').html($(this).html())
})

//搜索点击事件
$('.btn').click(function(){
	if($('.search input').val()){
		$('.result').hide();
		$('.search-content').show();
		$('.search-failure').hide();
	}else{
		$('.result').hide();
		$('.search-content').hide();
		$('.search-failure').show();
	}
	
})



// 反馈信息事件
$('.problem-solving .yes').mouseenter(function(){
	$('.problem-solving .yesHover').show();
	$('.problem-solving .yes-img').hide();
	$('.problem-solving .yes button').css('color','#02A65A');
});
$('.problem-solving .no').mouseenter(function(){
	$('.problem-solving .noHover').show();
	$('.problem-solving .no-img').hide();
	$('.problem-solving .no button').css('color','#FF5A3C');
});
$(".problem-solving .yes").mouseleave(function(){
    $('.problem-solving .yesHover').hide();
	$('.problem-solving .yes-img').show();
	$('.problem-solving .yes button').css('color','#999999');
});
$(".problem-solving .no").mouseleave(function(){
    $('.problem-solving .noHover').hide();
	$('.problem-solving .no-img').show();
	$('.problem-solving .no button').css('color','#999999');
});

// 笑脸是的点击事件
$('.problem-solving .yes').click(function(){
	$('.problem-solving .yesHover').show();
	$('.problem-solving .yes-img').hide();
	$('.problem-solving .yes button').css('color','#02A65A');
	$('.problem-solving .yes button').css('background','#E6F6EF');
	$('.yes-content').show();
	// $('.problem-solving').hide();


});
// 难过否的点击事件
$('.problem-solving .no').click(function(){
	$('.problem-solving .noHover').show();
	$('.problem-solving .no-img').hide();
	$('.no-content').show();
	$('.problem-solving .no button').css('color','#FF5A3C');
	$('.problem-solving .no button').css('background','#FFEFEC');

});

// 提交反馈信息事件
$("input[type='submit']").click(function(){
	$('.no-content').hide();
	$('.feedback').show();
	// 选中的单选按钮值
	console.log($(".checked input[type='radio']").val())
})

// 单选按钮点击事件

　　//给所有的单选按钮点击添加处理
$("input[type='radio']").click(function(){
　　 //找出和当前name一样的单选按钮对应的label，并去除选中的样式的class
　　$("input[type='radio']").parent().removeClass("checked");
　　　//给自己对应的label
　　$(this).parent().addClass("checked");
});
