let btn = document.getElementById("menu-button");
let screen = document.getElementById("screen");
let menu = document.getElementById("mobile_menu");

function open_close() {
  if (btn.dataset.menu === "0") myOpen();
  else myClose();
}

function myOpen() {
  menu.style.left = "0px";
  btn.dataset.menu = "1";
  btn.src = "/static/img/x-symbol_btn.svg"
  setTimeout((screen.style.backgroundColor = "rgb(200,200,200)"), 300);
}

function myClose() {
  menu.style.left = "-100%";
  btn.dataset.menu = "0";
  btn.style.backgroundColor = "transparent";
  screen.style.backgroundColor = "transparent";
  btn.src = "/static/img/hamber_btn.svg"
}

window.addEventListener("click", (e) => {
  if (e.target.className !== "submenu" && e.target !== btn) myClose();
});
/*
window.onload = function(){
  setTimeout(function(){
  document.querySelector('.loading').style.visibility = 'hidden'
  document.querySelector('.loading').style.opacity = 0
  },300);
};
*/

const mask = document.querySelector('.mask');
const html = document.querySelector('html');

html.style.overflow = 'auto';


window.addEventListener('DOMContentLoaded', function () {
  //아래 setTimeout은 로딩되는 과정을 임의로 생성하기 위해 사용. 실제 적용 시에는 삭제 후 적용해야함.
  setTimeout(function () {
    html.style.overflow = 'auto'; //스크롤 방지 해제
    mask.style.display = 'none';
  }, 2000);
})

