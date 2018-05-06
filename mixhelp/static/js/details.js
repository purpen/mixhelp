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



// 笑脸是的点击事件
$('.problem-solving .yes').click(function(){
	$('.problem-solving .yesHover').show();
	$('.problem-solving .yes button').css({'color':'#02A65A',});
	$('.problem-solving .yes button').css('background','#E6F6EF');
	$('.yes-content').show();
	// $('.problem-solving').hide();


});
// 难过否的点击事件
$('.problem-solving .no').click(function(){
	$('.problem-solving .noHover').show();
	$('.no-content').show();
	$('.problem-solving .no button').css('color','#FF5A3C');
	$('.problem-solving .no button').css('background','#FFEFEC');

});

// 提交反馈信息事件
// $("input[type='submit']").click(function(){
// 	$('.no-content').hide();
// 	$('.feedback').show();
// 	// 选中的单选按钮值
// 	console.log($(".checked input[type='radio']").val())
// })

// 单选按钮点击事件

　　//给所有的单选按钮点击添加处理
$("input[type='radio']").click(function(){
　　 //找出和当前name一样的单选按钮对应的label，并去除选中的样式的class
　　$("input[type='radio']").parent().removeClass("checked");
　　　//给自己对应的label
　　$(this).parent().addClass("checked");
});
