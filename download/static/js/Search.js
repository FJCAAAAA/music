//==>适应手机端的界面
var domContent = document.querySelector('html');//获取整个页面（dom）
var searctPendantPoint = document.getElementsByClassName('search-pendant-point')[0];//获取圆点（dom）
EventUtil.bindEvent(domContent, 'swipeleft', function () {
    searctPendantPoint.checked = true;
});//绑定左滑事件
EventUtil.bindEvent(domContent, 'swiperight', function () {
    searctPendantPoint.checked = false;
});

//==>监听按键事件
document.onkeydown = function (e) {
    var e = window.event ? window.event : e;
    //回车键登录
    if (e.keyCode == 13) goSearch();
}

//==>地址栏修改并跳转
function goURL(title, url) {
//    history.pushState(null, title, url);
    // 获取当前页面的协议（例如 "http:" 或 "https:"）
    const protocol = window.location.protocol;
    // 获取当前域名
    const hostname = window.location.hostname;
    // 你提供的URI部分，例如 "/new-path?query=123"
    // 构建完整的URL
    const newUrl = protocol + "//" + hostname + url;
    // 跳转到新的URL
    window.location.href = newUrl;
    document.title = title
}

//==>搜索事件
function goSearch() {
    var searchInput = document.getElementsByClassName('search-input')[0];
    var body = document.querySelector('body');
    if (searchInput.value) {
        body.classList.add("search-page");
        goURL("搜索 " + searchInput.value, "/search/?search_text=" + searchInput.value);//地址栏修改
    } else {
        body.classList.remove("search-page");
    }
}