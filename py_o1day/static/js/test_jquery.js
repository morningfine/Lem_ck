// jQuery在线手册： https://www.runoob.com/manual/jquery/
// jQuery在线手册： https://jquery.cuishifeng.cn/on.html

//这个函数中的js会等页面加载完成后才去执行
$(function (){
    // jquery 通过id获取元素
    // var box1 = $("#box1")
    // console.log(box1.text())

    // 通过属性过滤
    // var lis = $(".box3 li");
    // console.log(lis);

    // var lis = $(".box3 li[name='py']");
    // console.log(lis.text());

    // 选择父节点、子节点、兄弟节点
    // var li = $(".box3 li[name='py']");
    // 获取父节点
    // console.log(li.parent());

    // 获取子节点
    // console.log($(".box3").children());

    // 获取兄弟节点
    // console.log(li.siblings());

    // 获取前一个兄弟节点
    // console.log(li.prev().text());

    // 获取之前的所有兄弟节点
    // console.log(li.prevAll());

    // 获取之后的兄弟节点
    // console.log(li.next().text());

    // 选择之后的所有兄弟节点
    // console.log(li.nextAll());

    // 在某个元素下查找另一个元素
    // var aText = $(".box3").find("a").text();
    // console.log(aText);

    // 选择过滤
    // 选择包含p元素的div元素
    var aDiv = $("div").has("a");
    console.log(aDiv);

    // 选择包含p元素的div元素
    $("div").not(".box");

})