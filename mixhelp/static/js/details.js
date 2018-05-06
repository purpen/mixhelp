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
	var subdivide = $(this).html();
    $('.issueTemp ul li a').attr('href','/main/issue_list/' + subdivide)
	$('.subdivide-nav').html(subdivide)
	$('.subdivide-nav').attr('href','/main/issue_list' + subdivide)

	var num = $(this).attr('data-id')
	$('.issueTemp ul li a').attr('href','/main/issue_list/' + num)
	$('.subdivide-nav').attr('href','/main/issue_list/' + num)
	$('.particular-nav').attr('href','/main/issue_info/' + num)
})
$('.subdivide-nav').click(function () {
	var num = $(this).attr('data-id')
	$('.subdivide-nav').attr('href','/main/issue_list/' + num)
})




// 笑脸是的点击事件
$('.problem-solving .yes').click(function(){
	$('.problem-solving .yesHover').show();
	$('.problem-solving .yes button').css({'color':'#02A65A',});
	$('.problem-solving .yes button').css('background','#E6F6EF');
	$('.yes-content').show();
	// $('.problem-solving').hide();
	var url = window.location.pathname;
	var num = url.split('/')[3]
    $.post('/main/comment_yes',{'num':num},function (data) {
		if(data.res == 0){
			alert(data.message)
		}
    },
    "json"
    );
// 	$.ajax({
//         type:'GET',
//         url:'/api/v1.0/comment',
//         data:{'title':subdivide},
//         dataType:'json',//希望服务器返回json格式的数据
//         success:function(data){
//             alert(JSON.stringify(data));
//             alert(data['test'])
//         }
//     });

});
// 难过否的点击事件
$('.problem-solving .no').click(function(){
	$('.problem-solving .noHover').show();
	$('.no-content').show();
	$('.problem-solving .no button').css('color','#FF5A3C');
	$('.problem-solving .no button').css('background','#FFEFEC');

	var url = window.location.pathname;
	var num = url.split('/')[3]
    $.post('/main/comment_no',{'num':num},function (data) {
		if(data.res == 0){
			alert(data.message)
		}
    },
		'json'
	)

});

　　//给所有的单选按钮点击添加处理
$("input[type='radio']").click(function(){
　　 //找出和当前name一样的单选按钮对应的label，并去除选中的样式的class
　　$("input[type='radio']").parent().removeClass("checked");
　　　//给自己对应的label
　　$(this).parent().addClass("checked");
});

// $('.submit').click(function () {
// 	var issue_title = $('.particular h3').html()
//     $.post('/main/issue_cause',{'title':issue_title},function (data) {
// 		if(data.errno == 0){
// 			alert(data.errmsg)
// 		}
//     })
// })

window.onload=function(){
	$('.particular-content p img').attr('style', 'width: 80%;')

}

