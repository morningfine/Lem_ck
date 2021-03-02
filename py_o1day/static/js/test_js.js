window.onload = function (){

    //js选择页面
    var box1 = document.getElementById("box1");

    // 更改标签内容
    box1.innerText = "python1111";
    box1.innerHTML = "python2222";

    console.log(box1.innerText);
    console.log(box1.innerHTML);
}